from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    url(r'^snippets/$',views.Snippetlist.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$',views.Snippetdetail.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)