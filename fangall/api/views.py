from django.core.cache import caches
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.cache.decorators import cache_response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.exceptions import NotAuthenticated
from rest_framework.exceptions import AuthenticationFailed

from api.serializers import DistrictSerializer
from api.serializers import EstateSerializer
from api.serializers import HouseTypeSerializer
from common.models import District
from common.models import Estate
from common.models import HouseType
from common.models import User
from common.utils import gen_mobile_code
from common.utils import send_short_message


def mobile_code(request, tel):
    code = gen_mobile_code()
    send_short_message(tel, code)
    request.session['code'] = code
    caches['code'].set(tel, code, nx=True, timeout=60)
    return HttpResponse({'code': 200, 'msg': '验证码已经发送到您的手机'},
                        content_type='application/json; charset=utf-8')


# 第一种做法: 用@api_view()装饰视图函数
@cache_page(timeout=None, cache='page')
@api_view(['GET'])
def provinces(request):
    query_set = District.objects.filter(parent__isnull=True)
    serializer = DistrictSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)


@cache_page(timeout=1800, cache='page')
@api_view(['GET'])
def districts(request, pid):
    query_set = District.objects.filter(parent__distid=pid)
    serializer = DistrictSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "page"
    page_size_query_param = "size"


class Authentication(BaseAuthentication):

    def authenticate(self, request):
        try:
            userid = request.GET['userid']
            token = request.GET['token']
            user = User.objects.filter(userid=userid, token=token).first()
            if not user:
                raise AuthenticationFailed('用户身份信息认证失败')
            return user, user
        except KeyError:
            raise NotAuthenticated('请提供当前用户身份认证信息')

    def authenticate_header(self, request):
        pass


def customize_cache_key(view_instance, view_method, request, args, kwargs):
    """自定义缓存的key的函数"""
    full_path = request.get_full_path()
    return f'house:api:{full_path}'


# 第2种做法: 继承APIView及其子类根据需要重写方法或使用默认方法
class EstateView(ListCreateAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer
    # authentication_classes = [Authentication, ]

    # @cache_response(timeout=300, cache='page', key_func=customize_cache_key)
    def get(self, request, distid, *args, **kwargs):
        query_set = Estate.objects.filter(district__distid=distid)
        pager = MyPageNumberPagination()
        paged_query_set = pager.paginate_queryset(
            queryset=query_set, request=request, view=self)
        return pager.get_paginated_response(
            EstateSerializer(paged_query_set, many=True).data)


# 第3种做法: 继承ModelViewSet类
class HouseTypeViewSet(viewsets.ModelViewSet):
    queryset = HouseType.objects.all()
    serializer_class = HouseTypeSerializer
    pagination_class = None
