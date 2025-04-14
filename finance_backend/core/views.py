from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets, permissions, status
from .models import CustomUser, Transaction, TransactionCategory, Budget, LimitAlert
from .serializers import (
    CustomUserSerializer,
    TransactionSerializer,
    TransactionCategorySerializer,
    BudgetSerializer,
    LimitAlertSerializer,
)
from .permissions import IsAdminOrSelf, IsOwnerOrAdmin


class RegisterView(APIView):
    """
    Allows a new user to register and receive tokens.
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    Allows admin to manage all users. Regular users can only access their own account.
    """

    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSelf]

    def get_queryset(self):
        if self.request.user.is_staff:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise PermissionDenied("You do not have permission to create a user.")
        return super().create(request, *args, **kwargs)


class TransactionViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for user transactions.
    """

    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Transaction.objects.none()
        return Transaction.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to create transactions.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to update transactions.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to delete transactions.")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionCategoryViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for transaction categories.
    """

    serializer_class = TransactionCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return TransactionCategory.objects.none()
        return TransactionCategory.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to create categories.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to update categories.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to delete categories.")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BudgetViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for budgets per category.
    """

    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Budget.objects.none()
        return Budget.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to create budgets.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to update budgets.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to delete budgets.")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LimitAlertViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for limit alerts.
    """

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
    serializer_class = LimitAlertSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return LimitAlert.objects.none()
        return LimitAlert.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to create limit alerts.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to update limit alerts.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied("Admins are not allowed to delete limit alerts.")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
