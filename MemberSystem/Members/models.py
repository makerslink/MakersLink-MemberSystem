from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'surname']

    email = models.EmailField(unique=True, verbose_name="E-mail")
    firstname = models.CharField(max_length=100, verbose_name="Firstname", blank=False, null=False)
    surname = models.CharField(max_length=200, verbose_name="Surname", blank=False, null=False)