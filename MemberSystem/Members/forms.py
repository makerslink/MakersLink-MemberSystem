from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_registration.forms import RegistrationForm

from .models import Member

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = ('email',)

class MemberRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = Member
        fields = ('email','firstname','surname')