from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import get_user_model
from django.db.models import Q
# from django.contrib.auth.password_validation import validate_password

from user_api.models import User


class TokenSerializer(TokenObtainPairSerializer):
    credential = serializers.CharField(write_only=True)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token

    def validate(self, attrs):
        credential = attrs.get('credential', None)
        password = attrs.get('password', None)

        user = self._get_user(credential=credential, password=password)

        if not user:
            raise AuthenticationFailed("User not found or invalid credentials")

        UserModel = get_user_model()
        username_field = getattr(UserModel, "USERNAME_FIELD", "username")
        username_value = getattr(user, username_field, None)

        payload = {
            username_field: username_value,
            'password': password,
        }

        data = super().validate(payload)

        self.user = user
        user = self.user

        data.update({
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            # 'roles': [group.name for group in user.groups.all()],
        })
        return data

    def _get_user(self, credential, password):
        """
        Authenticate using email or username. Use a forgiving lookup for email.
        """
        if not credential or not password:
            return None

        user = User.objects.filter(
            Q(email__iexact=credential) | Q(username=credential)).first()

        if user and user.check_password(password):
            return user

        return None


# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(write_only=True, required=True)
#     new_password = serializers.CharField(
#         write_only=True, required=True, validators=[validate_password])
#     confirm_new_password = serializers.CharField(
#         write_only=True, required=True)

#     def validate(self, data):
#         """
#             Ensure old password is correct and new passwords match.
#         """
#         user = self.context['request'].user

#         if not user.check_password(data['old_password']):
#             raise serializers.ValidationError({"old_password": "Incorrect old password."})  # noqa

#         if data['new_password'] != data['confirm_new_password']:
#             raise serializers.ValidationError({"new_password": "New passwords do not match."})  # noqa

#         return data

#     def update(self, instance, validated_data):
#         """
#             Update user's password.
#         """
#         instance.set_password(validated_data['new_password'])
#         instance.save()
#         return instance
