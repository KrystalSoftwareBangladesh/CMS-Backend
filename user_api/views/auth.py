# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import permissions
# from rest_framework import status
# from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
# from rest_framework_simplejwt.tokens import RefreshToken

import logging

# from user_api.models import User

from user_api.serializers import TokenSerializer
# from user_api.serializers import ChangePasswordSerializer


logger = logging.getLogger(__name__)


class LoginView(TokenObtainPairView):
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        request.data['username'] = request.data.get('credential', None)
        request.data['email'] = request.data.get('credential', None)
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            response.data["message"] = "Login successful"

        return response


class TokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            response.data["message"] = "Access token refreshed successfully"

        return response
