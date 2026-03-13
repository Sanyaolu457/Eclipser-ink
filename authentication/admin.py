from django.contrib import admin
from .models import Participant
from django.contrib.auth.admin import UserAdmin

@admin.register(Participant)
class AdminParticipant(UserAdmin):
    list_display = ("username", "email", 'phone_number', "is_staff")
    search_fields = ("username", "email", 'phone_number')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    ordering = ("username",)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'user_permissions')}),
        ('Important dates', {'fields': ('date_joined',)}),
    )

    add_fieldsets = (
        (None, {
            'class': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'password1', 'password2')
        })
    )