from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'Members'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('Members:login')), name='logout'),
    path('password/change/', auth_views.PasswordChangeView.as_view(template_name="registration/change_password.html", success_url=reverse_lazy('Members:password_change_done')), name='password_change'),
    path('password/change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="registration/change_password_done.html"), name='password_change_done'),
    path('password/reset/', auth_views.PasswordResetView.as_view(template_name="registration/reset_password.html", success_url=reverse_lazy('Members:password_reset_done'), email_template_name='registration/email/password_reset_email.html'), name='password_reset'),
    path('password/reset/sent', auth_views.PasswordResetDoneView.as_view(template_name="registration/reset_password_sent.html"), name='password_reset_done'),
    path('password/reset/<uidb64>/<token>/confirm', auth_views.PasswordResetConfirmView.as_view(template_name="registration/reset_password_confirm.html", success_url=reverse_lazy('Members:password_change_done')), name='password_reset_confirm'),
]

# Views from django.auth
        # accounts/login/ [name='login']
        # accounts/logout/ [name='logout']
        # accounts/password_change/ [name='password_change']
        # accounts/password_change/done/ [name='password_change_done']
        # accounts/password_reset/ [name='password_reset']
        # accounts/password_reset/done/ [name='password_reset_done']
        # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
        # accounts/reset/done/ [name='password_reset_complete']
