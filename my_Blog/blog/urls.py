"""my_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.post_list , name = 'post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$' , views.post_list , name = 'post_list_by_tag'),
    # url(r'^$', views.PostListView.as_view() , name = 'post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_details , name = 'post_details'),
    url(r'^(?P<post_id>\d+)/share/', views.post_share , name = 'post_share'),
    url(r'^feed/$' , LatestPostsFeed() , name = 'post_feed'),
]
