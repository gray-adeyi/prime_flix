from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email: str, password: str, **extra_fields):
        """Create a user with the provided email and password"""
        email = sepf.normalize_email(email)
        user = self.model(email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email: str, password:str, **extra_fields):
        """Creates a superuser with the provided email and password"""
        extra_fields.set_default("is_admin",True)
        extra_fields.set_default("is_superuser",True)
        extra_fields.set_default("is_active",True)

        if extra_fields.get("is_admin") is False:
            raise ValueError(_("`is_admin` has to be set to `True` to create superuser"))
        if extra_fields.get("is_superuser") is False:
            raise ValueError(_("`is_superuser` has to be set to `True` to create superuser"))
        return self.create_user(email,password,**extra_fields)
