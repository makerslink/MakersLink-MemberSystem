from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from .forms import MemberRegistrationForm

urlpatterns = [
    path('register/', RegistrationView.as_view(form_class=MemberRegistrationForm), name='django_registration_register'),
    path('', include('django_registration.backends.activation.urls')),
]
