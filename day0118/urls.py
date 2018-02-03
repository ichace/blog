"""day0118 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
import ckeditor_uploader
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^blog-info/(\d+)/$',views.bk,name='bk'),
    url(r'^blog-fl/(\d+)/$',views.fl,name='fl'),
    url(r'^bq/(\d+)/$',views.bq,name='bq'),
    url(r'^ly/$',views.ly,name='ly'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)