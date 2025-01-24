# test_models.py
from django.test import TestCase
from .models import User
from django_cryptography.fields import encrypt

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password_hash='password123',
            full_name='Test User',
            phone_number='1234567890',
            address='123 Test St',
            account_status='Active'
        )

    def test_email_encryption(self):
        user = User.objects.get(username='testuser')
        self.assertNotEqual(user.email, 'test@example.com')
        self.assertTrue(user.email.startswith('gAAAAAB'))  # Encrypted strings typically start with 'gAAAAAB'

    def test_phone_number_encryption(self):
        user = User.objects.get(username='testuser')
        self.assertNotEqual(user.phone_number, '1234567890')
        self.assertTrue(user.phone_number.startswith('gAAAAAB'))

    def test_address_encryption(self):
        user = User.objects.get(username='testuser')
        self.assertNotEqual(user.address, '123 Test St')
        self.assertTrue(user.address.startswith('gAAAAAB'))