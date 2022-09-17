from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_("email address"), unique=True)
    is_admin = models.BooleanField(verbose_name=_("user is an admin"))
    is_active = models.BooleanField(verbose_name=_("user is active"))
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
