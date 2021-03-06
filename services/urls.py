"""services URL Configuration

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
import django.contrib
from django.urls import path
from categories import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'^', views.shoplist)

urlpatterns = [
    path('admin/', django.contrib.admin.site.urls),
    url(r'^categories/$', views.homepg, name='homepg'),
    url(r'^categories/(?P<Catg_id>[0-9])/$', views.type1, name='type1'),
    url(r'^categories/(?P<Catg_id>[0-9])/(?P<Type_id>[0-9]+)/$', views.prod, name='prod'),
    # url(r'^categories/(?P<Catg_id>[0-9])/(?P<Type_id>[0-9]+)/(?P<Product_id>[0-9]+)/$', views.ch, name='ch'),
    # url(r'^categories/(?P<Catg_id>[0-9])/(?P<Type_id>[0-9]+)/(?P<Product_id>[0-9]+)/(?P<Choice_id>[0-9]+)/$', views.Chatc, name='Chatc'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^categories/(?P<Catg_id>[0-9])/(?P<Type_id>[0-9]+)/shops/', include(router.urls)),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
