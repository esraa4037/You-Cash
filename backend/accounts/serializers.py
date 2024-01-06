from rest_framework import serializers
from accounts.models import Account



class AccountSerializer(serializers.ModelSerializer):
    class Meta(object): 
        model = Account
        fields = ["id", "first_name", "last_name", "username", "phone_num", "balance", "email"]
