from django.urls import path, include
from allauth.account.views import LogoutView

from .views import GoogleOAuthLoginView, signup_redirect

app_name = "accounts"

urlpatterns = [
    path("login/", GoogleOAuthLoginView.as_view(), name="login"),
    path("signup/", signup_redirect, name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", include("allauth.urls")),
]
