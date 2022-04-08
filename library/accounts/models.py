from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class LibraryAdminManager(BaseUserManager):
    """Manager for LibraryAdmin model."""

    def create_user(self, email, password, **extra_fields):
        """Create a new library user admin object

        :param email: User's email address
        :param password: User's password
        :returns: created user object
        """
        if not email:
            raise ValueError("The Email must be set")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class LibraryAdmin(AbstractUser):
    """LibraryAdmin is a cutomized user model that uses email as a username

    It also enforces unique constraints on email field.
    """

    username = None
    email = models.EmailField("email address", unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = LibraryAdminManager()

    def __str__(self):
        return self.email
