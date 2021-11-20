from django.urls import path
from .views import homepage

# URL Patterns
urlpatterns = [
    path('', homepage)
]
