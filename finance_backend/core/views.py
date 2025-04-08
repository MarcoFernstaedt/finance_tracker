from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from .models import CustomUser, Transaction, TransactionCategory, Budget
from .serializers import (
    CustomUserSerializer,
    TransactionSerializer,
    TransactionCategorySerializer,
    BudgetSerializer,
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
    Allows admin to view all users. Regular users can only access their own account.
    """

    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSelf]

    def get_queryset(self):
        if self.request.user.is_staff:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return Response(
                {"detail": "You do not have permission to create a user."},
                status=status.HTTP_403_FORBIDDEN,
            )


class TransactionViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for user transactions.
    """

    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Transaction.objects.all()
        return Transaction.objects.filter(user=self.request.user)

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
            return TransactionCategory.objects.all()
        return TransactionCategory.objects.filter(user=self.request.user)

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
            return Budget.objects.all()
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
