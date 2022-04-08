from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import LibraryAdmin


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="Provide a valid email.")

    class Meta:
        """extra information"""

        model = LibraryAdmin
        fields = (
            "email",
            "password1",
            "password2",
        )
