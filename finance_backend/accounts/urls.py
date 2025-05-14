from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView
from .views import RegisterView, LoginView, LogoutView, RefreshTokenView

urlpatterns = [
    path("auth/signin", LoginView.as_view(), name="login"),
    path("auth/register", RegisterView.as_view(), name="register"),
    path("auth/signout", LogoutView.as_view(), name="logout"),
    path("auth/refresh", RefreshTokenView.as_view(), name="refresh_token"),
    path("auth/verify", TokenVerifyView.as_view(), name="token_verify"),
]
