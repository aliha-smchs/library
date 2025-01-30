from django.db import models
from django.core.validators import MinLengthValidator



class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(2)])
    bio = models.TextField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),  # Index for faster lookups by name
        ]

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


