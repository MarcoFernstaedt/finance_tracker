from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    CustomUserViewSet,
    TransactionViewSet,
    TransactionCategoryViewSet,
    BudgetViewSet,
)

router = DefaultRouter()
router.register(r"users", CustomUserViewSet, basename="user")
router.register(r"transactions", TransactionViewSet, basename="Transaction")
router.register(r"category", TransactionCategoryViewSet, basename="Category")
router.register(r"budget", BudgetViewSet, basename="Budget")


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
