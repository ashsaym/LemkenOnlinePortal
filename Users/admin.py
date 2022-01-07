from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Users.models import Profile, CustomUser

from Users.forms import CustomUserCreationForm, CustomUserChangeForm, ProfileForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    readonly_fields = ('last_login', 'date_joined',)

    list_display = (
        'email', 'is_staff', 'is_superuser', 'is_active', 'is_seller', 'is_external', 'last_login', 'date_joined',)
    list_filter = (
        'email', 'is_staff', 'is_superuser', 'is_active', 'is_seller', 'is_external', 'last_login', 'date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Site Permissions', {'fields': ('is_staff', 'is_superuser')}),
        ('Role', {'fields': ('is_seller', 'is_external')}),
        ('Activities', {'classes': ('collapse',),
                        'fields': ('is_active', 'last_login', 'date_joined')}),
        ('User Permissions', {
            'classes': ('collapse',),
            'fields': ('user_permissions',)
        }),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_seller', 'is_external')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
