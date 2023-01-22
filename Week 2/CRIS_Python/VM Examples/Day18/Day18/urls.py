"""Day18 URL Configuration

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
from MyApp import views


urlpatterns = [
    url(r'^index/', views.index),
    url(r'^CustomerSave/', views.CustomerSave),
    url(r'^ShowData/', views.ShowData),
    url(r'^ShowData2/', views.ShowData2),
    url(r'^test/', views.test),
    #following two urls meant for AJAX
    url(r'^test2/', views.test2),
    url(r'^test_ajax_script/', views.test_ajax_script),

    url(r'^sessiontest/', views.sessiontest),
    url(r'^sessiontest2/', views.sessiontest2),

    url(r'^admin/', admin.site.urls),

]

