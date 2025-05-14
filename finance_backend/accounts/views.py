from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError
from .serializers import CustomTokenObtainPairSerializer


# Register new user and return access token + set refresh cookie
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        User = get_user_model()
        try:
            if User.objects.filter(email=data.get("email")).exists():
                return Response(
                    {"error": "Email already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user = User.objects.create_user(
                name=data.get("name"),
                email=data.get("email"),
                password=data.get("password"),
            )

            refresh = RefreshToken.for_user(user)

            res = Response(
                {
                    "access": str(refresh.access_token),
                    "user": {"id": user.id, "name": user.name, "email": user.email},
                },
                status=status.HTTP_201_CREATED,
            )

            res.set_cookie(
                key="refresh_token",
                value=str(refresh),
                httponly=True,
                secure=False,  # Set to True in production
                samesite="Lax",
            )

            return res
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# Login view — returns access token and sets refresh cookie
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data.get("refresh")

        if refresh:
            response.set_cookie(
                key="refresh_token",
                value=refresh,
                httponly=True,
                secure=False,  # Set to True in production
                samesite="Lax",
            )
            del response.data["refresh"]

        return response


# Refresh access token using the refresh token in cookies
class RefreshTokenView(APIView):
    def post(self, request):
        token = request.COOKIES.get("refresh_token")
        if not token:
            return Response(
                {"error": "Refresh token not provided"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        try:
            refresh_token = RefreshToken(token)
            return Response(
                {"access": str(refresh_token.access_token)}, status=status.HTTP_200_OK
            )
        except TokenError:
            return Response(
                {"error": "Invalid or expired token"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


# Logout — removes the refresh_token cookie
class LogoutView(APIView):
    def post(self, request):
        response = Response(
            {"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT
        )
        response.delete_cookie("refresh_token")
        return response
