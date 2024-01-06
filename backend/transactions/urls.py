from django.urls import path
from . import views

urlpatterns = [
    path("credit", views.credit, name="credit"),
    path("debit", views.debit, name="debit"),
    path("transfer", views.transfer, name="transfer"),
]
