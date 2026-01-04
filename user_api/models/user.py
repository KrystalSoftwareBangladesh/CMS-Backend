from django.db import models

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser, BaseUserManager  # noqa


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)  # noqa
    is_deleted = models.BooleanField(default=False)
    added_at = models.DateTimeField(_('Added Date Time'), auto_now_add=True,)
    updated_at = models.DateTimeField(_('Updated Date Time'), auto_now=True,)

    objects = UserManager()

    # USERNAME_FIELD = 'username'
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']
    REQUIRED_FIELDS = []

    @property
    def full_name(self) -> str:
        """
            Returns full name combining first, middle, and last name.
        """
        return " ".join(filter(None, [
            self.first_name, self.middle_name, self.last_name
        ]))

    def __str__(self):
        return self.full_name
