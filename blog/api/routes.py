from django.urls import path

from .views import api_blog_list

urlpatterns = [
    path('', api_blog_list, name='blog_api_list'),
]