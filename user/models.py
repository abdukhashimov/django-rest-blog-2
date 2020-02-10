from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_args):
        """Creates and saves the user with the given email, and password"""
        if not email:
            raise ValueError('Users must have an emaild address!')

        user = self.model(
            email=self.normalize_email(email), **extra_args)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """Creates and saves superuser using email"""
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def get_profile_picture(self):
        return "http://localhost:8000" + self.profile.profile_picture.url


class UserInfo(models.Model):
    profile_user = models.OneToOneField(
        get_user_model(), related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_picture', blank=True, null=True)

    def __str__(self):
        return str(self.profile_user)
