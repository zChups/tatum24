from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance.user:
            self.fields['email'].initial = self.instance.user.email

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.exclude(pk=self.instance.user.pk).filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please choose another.")
        return email

    def save(self, commit=True):
        user = self.instance.user
        if user:
            user.email = self.cleaned_data['email']
            user.save()
        return super(UserProfileForm, self).save(commit=commit)
