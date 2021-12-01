from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from .views import *



# URL Patterns
urlpatterns = [
    path("", homepage, name="blog_list"),
    path("<slug:slug>/", blog_detail, name="blog_detail"),
    # path('login', user_login, name='login'),
    path("login", LoginView.as_view(), name="login"),
    path("register", register, name="register"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("password-change", PasswordChangeView.as_view(), name="password-reset"),
    path(
        "password-change/done",
        PasswordChangeDoneView.as_view(),
        name="password-reset-done",
    ),
    path('add-posts', add_article, name='add_posts'),
    path('update/<slug:slug>', update_article, name='update_posts'),
    path('delete/<slug:slug>', delete_article, name='delete_posts'),

]

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Perykun Blog API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@perykun.xyz"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# API Url Patterns
api_urlpattens = [
    path('api/v1/blog/', include('blog.api.routes')),
    path('docs/api/v1/blog/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]

urlpatterns += api_urlpattens
