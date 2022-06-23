from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    # firstname = forms.CharField(max_length=255)
    # lastname = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ["username", "email", 'password1', 'password2', 'first_name', 'last_name']

    def save(self, commit=True, **kwargs):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        print(self.cleaned_data["username"])
        print(self.cleaned_data["email"])
        print(self.cleaned_data["password1"])
        print(self.cleaned_data["first_name"])
        print(self.cleaned_data["last_name"])
        if commit:
            print("Received form")
            user.save()
        return user
