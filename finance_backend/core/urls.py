from django.urls import path
from rest_framework_simplejwt.views import { TokenObtainPairView, TokenRefreshView}
from .views import ping

urlpatterns = [
    path("ping/", ping, name="ping"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),,
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
