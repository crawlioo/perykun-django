from django.urls import path
from .views import *

# URL Patterns
urlpatterns = [
    path('', homepage, name='blog_list'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),
    path('login', user_login)
]
