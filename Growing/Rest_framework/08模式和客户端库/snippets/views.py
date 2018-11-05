from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import permissions
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action


@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'users':reverse('user-list',request=request,format=format),
        'snippets':reverse('snippet-list',request=request,format=format)
    })



class SnippetViewSet(viewsets.ModelViewSet):

        # viewset自动提供"list","retrieve","update","destory","create" 方法

        # 也自动提供额外的高亮方法

        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerReadOnly)

        @action(detail=True,renderer_classes=[renderers.StaticHTMLRenderer])
        def highlight(self, request, *args, **kwargs):
            snippet = self.get_object()
            return Response(snippet.highlighted)


        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)




class UserViewSet(viewsets.ReadOnlyModelViewSet):

    # viewset自动提供"list"和"detail"动作

    queryset = User.objects.all()
    serializer_class = UserSerializer



















