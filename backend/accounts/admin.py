from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "phone_num",
        "is_staff",
        "balance",
    )
    list_display_links = ("id", "username")
    search_fields = ("username", "phone_num")


admin.site.register(Account, AccountAdmin)
