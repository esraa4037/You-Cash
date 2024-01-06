from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

 
class Account(AbstractUser):
    phone_num = models.CharField(max_length=11, unique=True, null=True)
    balance = models.DecimalField(
        default=0,
        max_digits=7,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(100000)],
    )

    def __str__(self):
        return str(self.phone_num)

    def save(self, *args, **kwargs):
        if self.balance < 0 or self.balance > 100000:
            raise ValidationError("Balance must be between 0 and 100000.")

        super().save(*args, **kwargs)

