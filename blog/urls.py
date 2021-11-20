from django.urls import path
from .views import homepage, blog_detail

# URL Patterns
urlpatterns = [
    path('', homepage, name='blog_list'),
    path('<slug:slug>/', blog_detail, name='blog_detail')
]
