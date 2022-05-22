from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    list_display = UserAdmin.list_display + (
        "avatar",
        "gender",
        "bio",
        "language",
        "currency",
        "birthdate",
        "superhost",
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "language",
                    "currency",
                    "birthdate",
                    "superhost",
                )
            },
        ),
    )
