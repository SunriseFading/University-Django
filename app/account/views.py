from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from account.models import CustomUser


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = CustomUser.objects.filter(email=email).first()
        if user and user.check_password(password):
            if user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=200)
            else:
                return Response({"error": "Removed"}, status=410)
        else:
            return Response({"error": "Invalid login credentials"}, status=400)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        Token.objects.filter(user=request.user).delete()
        return Response(status=200)
