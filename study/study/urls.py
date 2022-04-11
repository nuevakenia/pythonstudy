"""study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.urls.conf import re_path
from django.views.generic import TemplateView
from study.core.views import Test1View, CalcView
from study.core.views import frontendRender_view

# Create your views here.

app_name = 'study'

urlpatterns = [
    # User management
    #re_path(r'(?P<path>.*)', Test1View.as_view(), name='home'),
    path("core/", include("study.core.urls", namespace="core")),
    path('admin/', admin.site.urls),
    path('test', TemplateView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include("study.api_router")),
    #re_path(r'^api/', include("study.api_router")),
]

urlpatterns += [
    #re_path(r'(?P<path>.*)', frontendRender_view, name='home')
]
