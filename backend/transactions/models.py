from django.db import models
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError
from accounts.models import Account
 
class Transaction(models.Model):
    trans_type_choices = [ 
        ("debit", "Debit"),
        ("credit", "Credit"),
        ("transfer", "Transfer"),
    ]

    account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, related_name="transaction", null=True
    )
    transaction_type = models.CharField(max_length=20, choices=trans_type_choices)
    transaction_date = models.DateTimeField(default=datetime.now)
    amount = models.DecimalField(
        max_digits=7,
        decimal_places=1,
        validators=[MinValueValidator(5), MaxValueValidator(30000)],
    )

    def __str__(self):
        return self.transaction_type

    def save(self, *args, **kwargs):
        if self.amount < 5 or self.amount > 30000:
            raise ValidationError("Amount must be between 5 and 30000.")

        super().save(*args, **kwargs)


class Transfer(Transaction):
    receiver_account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, related_name="receive", null=True
    )
