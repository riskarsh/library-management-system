from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class LibraryAdminManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class LibraryAdmin(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = LibraryAdminManager()

    def __str__(self):
        return self.email
