from .models import CustomUser, Transaction, TransactionCategory, Budget
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model.
    Handles user creation and JWT token generation.
    """

    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password", "token", "is_staff"]
        extra_kwargs = {"password": {"write_only": True}}

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}

    def create(self, validated_data):
        return CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )


class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for Transaction model.
    Includes read-only fields for user, created_at, updated_at.
    """

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["user", "created_at", "updated_at"]


class TransactionCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for TransactionCategory model.
    Includes read-only fields for user, created_at, updated_at.
    """

    class Meta:
        model = TransactionCategory
        fields = "__all__"
        read_only_fields = ["user", "created_at", "updated_at"]


class BudgetSerializer(serializers.ModelSerializer):
    """
    Serializer for Budget model.
    Includes read-only fields for user, created_at, updated_at.
    """

    class Meta:
        model = Budget
        fields = "__all__"
        read_only_fields = ["user", "created_at", "updated_at"]
