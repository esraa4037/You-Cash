from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .models import Account
from .serializers import AccountSerializer
from transactions.serializers import TransactionSerializer
from transactions.models import Transaction, Transfer
from accounts.permissions import IsOwnerOrAdmin


@api_view(["POST"])
def register(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        account = Account.objects.get(username=request.data["username"])
        account.set_password(request.data["password"])
        account.save()
        token = Token.objects.create(user=account)
        return Response({"token": token.key, "account": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    account = get_object_or_404(Account, phone_num=request.data["phone_num"])
    if not account.check_password(request.data["password"]):
        return Response(
            {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )

    token, created = Token.objects.get_or_create(user=account)
    serializer = AccountSerializer(instance=account)
    return Response({"token": token.key, "account": serializer.data})


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.user.is_authenticated:
        Token.objects.filter(user=request.user).delete()
        return Response({"detail": "Logged out successfully."})
    return Response({"detail": "User is not authenticated."}, status=401)


# Get transacion history for a specific account
@api_view(["GET"])
# @permission_classes([IsOwnerOrAdmin])
# @authentication_classes([TokenAuthentication])
def transaction_history(request, account_id):
    try:
        account = Account.objects.get(id=account_id)
    except Account.DoesNotExist:
        raise Http404

    transactions = account.transaction.all()
    received = account.receive.all()
    all_transactions = list(transactions) + list(received)
    sorted_transactions = sorted(
        all_transactions, key=lambda x: x.transaction_date, reverse=True
    )

    serializer = TransactionSerializer(sorted_transactions, many=True)
    return Response({"list": serializer.data})


# Get account by id
@api_view(["GET"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsOwnerOrAdmin])
# @permission_classes([IsAuthenticated])
def account_details(request, account_id):
    try:
        account = Account.objects.get(id=account_id)
        serializer = AccountSerializer(account)
        return Response({"account": serializer.data})
    except Account.DoesNotExist:
        return JsonResponse({"error": "Account not found"}, status=404)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.username))
