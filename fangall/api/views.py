from django.core.cache import caches
from django.core.cache import cache
from django.db import connection
from django.db.models import Manager
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from pymysql import MySQLError
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_extensions.cache.decorators import cache_response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.exceptions import NotAuthenticated
from rest_framework.exceptions import AuthenticationFailed

from api.serializers import DistrictSerializer, AgentDetailSerializer
    # , AgentListSerializer

from api.serializers import EstateSerializer
from api.serializers import HouseTypeSerializer
from common.models import District, Agent
from common.models import Estate
from common.models import HouseType
from common.models import User
from common.utils import gen_mobile_code
from common.utils import send_short_message


def mobile_code(request, tel):
    code = gen_mobile_code()
    send_short_message.delay(tel, code)
    request.session['code'] = code
    # redis_client = get_redis_connection(alias='code')
    # print(redis_client)
    caches['code'].set(tel, code, nx=True, timeout=60)
    # cache.set(tel, code, nx=True, timeout=60)
    return HttpResponse({'code': 200, 'msg': '验证码已经发送到您的手机'},
                        content_type='application/json; charset=utf-8')


def customize_cache_key(view_instance, view_method, request, args, kwargs):
    """自定义缓存的key的函数"""
    full_path = request.get_full_path()
    return f'fangall:api:{full_path}'


# 第一种做法: 用@api_view()装饰视图函数
@api_view(['GET'])
@cache_page(timeout=None)
def provinces(request):
    query_set = District.objects.filter(parent__isnull=True)
    serializer = DistrictSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@cache_page(timeout=120)
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
                raise NotAuthenticated('用户身份认证失败')
            return user, user
        except KeyError:
            raise NotAuthenticated('请提供当前用户身份认证信息')

    def authenticate_header(self, request):
        pass


# 第2种做法: 继承APIView及其子类根据需要重写方法或使用默认方法
class EstateView(ListCreateAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer
    authentication_classes = [Authentication, ]

    # drf-extensions
    @cache_response(key_func=customize_cache_key)
    def get(self, request, distid, *args, **kwargs):
        query_set = Estate.objects.filter(district__distid=distid)
        pager = MyPageNumberPagination()
        paged_query_set = pager.paginate_queryset(
            queryset=query_set, request=request, view=self)
        return pager.get_paginated_response(
            EstateSerializer(paged_query_set, many=True).data)


# 第3种做法: 继承ModelViewSet类
class HouseTypeViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = HouseType.objects.all()
    serializer_class = HouseTypeSerializer
    pagination_class = None


class AgentDetailView(ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentDetailSerializer
    authentication_classes = [Authentication, ]
    pagination_class = None

    @cache_response(key_func=customize_cache_key)
    def get(self, request, agentid, *args, **kwargs):
        query_set = Agent.objects.filter(agentid=agentid)\
            .prefetch_related("estates").last()
        serializer = AgentDetailSerializer(query_set)
        return Response(serializer.data)


# class AgentViewSet(viewsets.ModelViewSet):
#
#     queryset = Agent.objects.all()
#     serializer_class = AgentListSerializer



