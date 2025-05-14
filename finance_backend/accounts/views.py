from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.simplejwt.tokens import RefreshToken


# Create your views here.
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
                samesite="lax",
            )

            return res
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
