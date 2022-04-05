from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import MemberManager

# Custom user model with no username only email
class Member(AbstractUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'surname']

    objects = MemberManager()

    # Remove username field
    username = None
    email = models.EmailField(unique=True, verbose_name="E-mail")
    firstname = models.CharField(max_length=100, verbose_name="Firstname", blank=False, null=False)
    surname = models.CharField(max_length=200, verbose_name="Surname", blank=False, null=False)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'