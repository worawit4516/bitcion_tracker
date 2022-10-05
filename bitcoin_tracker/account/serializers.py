from rest_framework import serializers
from historical_data.models import PriceHistory
from account.models import Account
from historical_data.serializers import PriceHistorySerializer
from django.db.models import OuterRef, Subquery, Sum

import json


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name'
        )


class AccountHistorySerializer(serializers.ModelSerializer):
    histories = serializers.SerializerMethodField()
    stat = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'stat',
            'histories'
        )

    def get_histories(self, account):
        price_histories = PriceHistory.objects.filter(user=account.id)
        # account_histories = account.PriceHistory_set.all()
        serializer_account_histories = PriceHistorySerializer(price_histories, many=True)
        return serializer_account_histories.data

    def get_stat(self, account):
        price_histories = PriceHistory.objects.filter(user=account.id)
        amount_price = 0
        for history in price_histories:
            amount_price += history.price
        avg_price = amount_price / len(price_histories)
        amount_history = len(price_histories)
        stat = {
            'amount_price': amount_price,
            'avg_price': avg_price,
            'amount_history': amount_history
        }
        return stat