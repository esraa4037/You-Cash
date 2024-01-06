from django.contrib import admin
from .models import Transaction, Transfer


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "transaction_type",
        "transaction_date",
        "amount",
    )
    list_display_links = ("id", "transaction_type")


class TransferAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "transaction_type",
        "transaction_date",
        "amount",
    )
    list_display_links = ("id", "transaction_type")


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Transfer, TransferAdmin)
