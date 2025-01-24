# forms.py
# forms.py
from django import forms
from django.contrib.auth.hashers import make_password
from django_cryptography.fields import encrypt

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password_hash',
            'full_name',
            'phone_number',
            'address',
            'account_status'
        ]
        widgets = {
            'password_hash': forms.PasswordInput(),  # Use a password input widget for the password field
            'email': forms.EmailInput(),             # Use an email input widget for the email field
            'phone_number': forms.TextInput(),       # Use a text input widget for the phone number field
            'address': forms.Textarea(),             # Use a textarea widget for the address field
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders or custom attributes to form fields (optional)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter email'})
        self.fields['password_hash'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['full_name'].widget.attrs.update({'placeholder': 'Enter full name'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Enter phone number'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Enter address', 'rows': 3})


    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password before saving
        user.password_hash = make_password(self.cleaned_data['password_hash'])
        if commit:
            user.save()
        return user