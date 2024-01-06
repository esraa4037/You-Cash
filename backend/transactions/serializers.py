from rest_framework import serializers
from transactions.models import Transaction
 

class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    transaction_type = serializers.CharField()
    transaction_date = serializers.DateTimeField()
    amount = serializers.DecimalField(max_digits=7, decimal_places=1)
    # account_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Transaction.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.transaction_type = validated_data.get(
            "transaction_type", instance.transaction_type
        )
        instance.transaction_date = validated_data.get(
            "transaction_date", instance.transaction_date
        )
        instance.amount = validated_data.get("amount", instance.amount)
        instance.save()
        return instance
