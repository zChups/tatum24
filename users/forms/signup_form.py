import re
from django.contrib.auth.models import User
from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(render_value=False)
    )
    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(render_value=False)
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already in use. Please choose another.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please choose another.")
        return email

    # Password check

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError("The password must be at least 8 characters long.")
        if not re.search(r'\d', password1):
            raise forms.ValidationError("The password must contain at least one digit.")
        if not re.search(r'[A-Za-z]', password1):
            raise forms.ValidationError("The password must contain at least one letter.")
        if not re.search(r'[A-Z]', password1):
            raise forms.ValidationError("The password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password1):
            raise forms.ValidationError("The password must contain at least one lowercase letter.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
            raise forms.ValidationError("The password must contain at least one special character.")
        return password1

    def clean(self):  # Passwords match
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']

        new_user = User.objects.create_user(username=username, email=email, password=password)
        return new_user
