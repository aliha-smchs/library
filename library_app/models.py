import datetime
from django.db import models
from django.db.models import Q, F
from django.db.models.constraints import CheckConstraint, UniqueConstraint
from django.db.models.expressions import RawSQL
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import JSONField  # For tags in PostgreSQL (Django 3.1+)
from django_cryptography.fields import encrypt
# --------------------------------------------------
# 1. Users
# --------------------------------------------------
class User(models.Model):
    ACCOUNT_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Suspended', 'Suspended'),
        ('Inactive', 'Inactive'),
    ]

    user_id = models.AutoField(primary_key=True, db_column='user_id')
    username = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    password_hash = encrypt(models.CharField(max_length=255))
    full_name = models.CharField(max_length=100)
    phone_number = encrypt(models.CharField(max_length=20, null=True, blank=True))
    address = encrypt(models.TextField(null=True, blank=True))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    account_status = models.CharField(max_length=9,choices=ACCOUNT_STATUS_CHOICES,default='Active')

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        # Normalize email and encrypt before saving
        if self.email:
            self.email = self.email.strip().lower()
            self.email = encrypt(self.email)
        super().save(*args, **kwargs)

# --------------------------------------------------
# 2. Memberships & Payments
# --------------------------------------------------
