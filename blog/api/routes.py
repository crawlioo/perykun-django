from django.urls import path

from .views import api_blog_list, api_blog_detail

urlpatterns = [
    path('', api_blog_list, name='api_blog_list'),
    path('<slug:slug>', api_blog_detail, name='api_blog_detail')
]