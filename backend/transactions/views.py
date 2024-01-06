from django.shortcuts import render
from django.contrib import messages
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from django.http import Http404
from decimal import Decimal

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
 
from accounts.permissions import IsOwnerOrAdmin
from accounts.models import Account
from transactions.models import Transaction, Transfer
from transactions.serializers import TransactionSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def credit(request):
    account = request.user
    amount = Decimal(request.data.get("amount"))
    password = request.data.get("password") 

    if not account.check_password(password):
        return Response(
            {"detail": "Incorrect Password."}, status=status.HTTP_403_FORBIDDEN
        )

    try:
        # Credit
        with transaction.atomic():
            # Create transaction
            new_transaction = Transaction()
            new_transaction.account = account
            new_transaction.transaction_type = "credit"
            new_transaction.amount = amount
            new_transaction.save()

            # increase the account balance
            account.balance += amount
            account.save()

        serializer = TransactionSerializer(instance=new_transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        error_message = e.message or "Validation Error"
        return Response({"detail": error_message}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def debit(request):
    account = request.user
    amount = Decimal(request.data.get("amount"))
    password = request.data.get("password")

    if not account.check_password(password):
        return Response(
            {"detail": "Incorrect Password."}, status=status.HTTP_403_FORBIDDEN
        )

    try:
        # Debit
        with transaction.atomic():
            # Create transaction
            new_transaction = Transaction()
            new_transaction.account = account
            new_transaction.transaction_type = "debit"
            new_transaction.amount = amount
            new_transaction.save()

            # decrease the account balance
            account.balance -= amount
            account.save()

        serializer = TransactionSerializer(instance=new_transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        error_message = e.message or "Validation Error"
        return Response({"detail": error_message}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def transfer(request):
    sender = request.user
    receiver = get_object_or_404(Account, phone_num=request.data["to"])
    amount = Decimal(request.data.get("amount"))
    password = request.data.get("password")

    if not sender.check_password(password):
        return Response(
            {"detail": "Incorrect Password."}, status=status.HTTP_403_FORBIDDEN
        )
        
    if sender.phone_num == receiver.phone_num:
        return Response(
            {"detail": "Transfer to the same account."}, status=status.HTTP_400_BAD_REQUEST
        )
        

    try:
        # Transfer
        with transaction.atomic():
            # Create transaction
            new_transaction = Transfer()
            new_transaction.account = sender
            new_transaction.transaction_type = "transfer"
            new_transaction.amount = amount
            new_transaction.save()

            # decrease the sender balance
            sender.balance -= amount
            sender.save()

            # increase the receiver balance
            receiver.balance += amount
            receiver.save()

        serializer = TransactionSerializer(instance=new_transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        error_message = e.message or "Validation Error"
        return Response({"detail": error_message}, status=status.HTTP_400_BAD_REQUEST)

