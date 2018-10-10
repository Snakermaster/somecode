from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from snippets import views
from rest_framework.schemas import get_schema_view




# 创建一个router 然后注册viewset
router = DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)

schema_view = get_schema_view(title="Pastebin API")

urlpatterns = [
    url(r'api_auth/$',include('rest_framework.urls')),
    url(r'^',include(router.urls)),
    url(r'^schema/$',schema_view),
]
