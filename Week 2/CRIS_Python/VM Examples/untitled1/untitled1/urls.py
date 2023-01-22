"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from VideoLib import views
urlpatterns = [
    url(r'^indexDelete/', views.indexDelete),
    url(r'^indexResult/', views.indexResult),
    url(r'^indexResult2/', views.indexResult2),
    url(r'^indexProcess/', views.indexProcess),
    url(r'^pie3D/', views.pie3D),
    url(r'^pie3D_ajax_script/', views.pie3D_ajax_script),
    url(r'^pie3D_ajax_script_smart/', views.pie3D_ajax_script_smart),
    url(r'^testsession/', views.testsession),
    url(r'^testsession2/', views.testsession2),
    url(r'^index/', views.index),
    url(r'^admin/', admin.site.urls),
]
