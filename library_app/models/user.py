from django.core.validators import EmailValidator
from django.contrib.auth.models import AbstractUser
from .textfield import EncryptedTextField
from django.db import models
from .role import Role

class User(AbstractUser):
    username = EncryptedTextField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Use Django's built-in auth for hashing
    email = EncryptedTextField(unique=True, validators=[EmailValidator()])
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['username']),  # Index for faster username lookups
            models.Index(fields=['email']),     # Index for faster email lookups
        ]

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=20)
    phone_number = EncryptedTextField(max_length=15)

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)  # e.g., Librarian, Admin
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

