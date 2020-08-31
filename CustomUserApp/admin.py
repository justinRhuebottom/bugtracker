from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from CustomUserApp.models import MyUser

class CustomUserAdmin(UserAdmin):
    UserAdmin.fieldsets = (
        (
            'Custom Fields',{
                'fields': ('display_name',),
            },
        ),
    )

admin.site.register(MyUser, CustomUserAdmin)