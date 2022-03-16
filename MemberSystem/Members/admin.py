from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Member

# Register your models here.
class MemberAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Member
    list_display = ('email','firstname','surname', 'is_staff', 'is_superuser', 'is_active',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal information', {'fields': ('firstname','surname')}),
        ('Permissions', {'fields': ('is_staff','is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'firstname','surname', 'is_staff', 'is_superuser', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Member, MemberAdmin)
