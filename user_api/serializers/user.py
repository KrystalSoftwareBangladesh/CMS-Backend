from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from user_api.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        # required=True,
        required=False,
        validators=[validate_password],
    )
    confirm_password = serializers.CharField(
        write_only=True,
        # required=True,
        required=False,
    )

    class Meta:
        model = User
        fields = [
            'id', 'full_name', 'first_name', 'middle_name', 'last_name',
            'email', 'username', 'password', 'confirm_password', 'groups',
        ]
        read_only_fields = ['id',]
        write_only = ['password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        """Dynamically modify fields based on request method."""
        super().__init__(*args, **kwargs)
        request = self.context.get('request')   # noqa

    def to_representation(self, instance):
        """
            Modify response to always return full_name instead of separate
            name fields.
        """
        data = super().to_representation(instance)

        data.pop('first_name', None)
        data.pop('middle_name', None)
        data.pop('last_name', None)

        return data

    # def validate(self, data):
    #     return data

    # def _create_validation(self, data):
    #     if not data.get('username', None):
    #         data['username'] = data.get('email', None)

    #     if not data.get('username', None):
    #         raise serializers.ValidationError({"username": "Username required"})    # noqa

    #     if not data.get('email', None):
    #         raise serializers.ValidationError({"email": "Email required"})

    #     password = data.get('password', None)
    #     confirm_password = data.get('confirm_password', None)

    #     # if not password or not confirm_password:
    #     #     raise serializers.ValidationError({
    #     #         "password": "Password and Confirm Password both required",
    #     #     })

    #     if password != confirm_password:
    #         raise serializers.ValidationError({
    #             "password": "Password do not match"
    #         })

    # def create(self, validated_data):
    #     """
    #         Create a new user and assign a role.
    #     """
    #     self._create_validation(data=validated_data)

    #     validated_data.pop('confirm_password', None)
    #     groups = validated_data.pop('groups', [])

    #     password = validated_data.pop('password', None)
    #     # user = User.objects.create_user(**validated_data)
    #     user = User(**validated_data)

    #     if password:
    #         user.set_password(password)
    #     else:
    #         user.set_unusable_password()

    #     user.save()
    #     user.groups.set(groups)

    #     return user

    # def update(self, instance, validated_data):
    #     validated_data.pop('password', None)
    #     validated_data.pop('confirm_password', None)
    #     groups = validated_data.pop('groups', None)

    #     user = super().update(instance, validated_data)
    #     if groups is not None:
    #         user.groups.set(groups)
    #     return user
