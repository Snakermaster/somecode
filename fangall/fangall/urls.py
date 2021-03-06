"""fangall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rent import views

urlpatterns = [
    path('', views.home, name='index'),
    path('api/', include('api.urls')),
    path('common/', include('common.urls')),
    path('rent/', include('rent.urls')),
    path('user/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:

    import debug_toolbar

    urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))
