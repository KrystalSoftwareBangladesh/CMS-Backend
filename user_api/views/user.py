from rest_framework import generics, permissions

from user_api.serializers import UserProfileSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
            Return the authenticated user.
        """
        return self.request.user

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
