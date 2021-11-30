from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import path, include

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
    path('api/', include('blog.api.routes')),

]

# API Url Patterns
# api_urlpattens = {
#     path('api/', include('blog.api.routes')),
# }
#
# urlpatterns += api_urlpattens
