from rest_framework import serializers
from historical_data.models import PriceHistory
from account.models import Account
from wallet.models import Wallet
from historical_data.serializers import PriceHistorySerializer
from wallet.serializers import WalletCreateSerializer, WalletDetailSerializer
from django.db.models import OuterRef, Subquery, Sum

import json


class AccountSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField()
    wallet = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'friends',
            'wallet'
        )

        def get_friends(self, account):
            friends = json.loads(account.friends)
            return friends

        def get_wallet(self, account):
            wallet = Wallet.objects.filter(user=account.id)
            # account_histories = account.PriceHistory_set.all()
            serializer_wallet = WalletDetailSerializer(wallet, many=True)
            return serializer_wallet


class AccountHistorySerializer(serializers.ModelSerializer):
    histories = serializers.SerializerMethodField()
    stat = serializers.SerializerMethodField()
    friends = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'stat',
            'histories',
            'friends'
        )

    def get_friends(self, account):
        friends = json.loads(account.friends)
        return friends

    def get_histories(self, account):
        price_histories = PriceHistory.objects.filter(user=account.id)
        # account_histories = account.PriceHistory_set.all()
        serializer_account_histories = PriceHistorySerializer(price_histories, many=True)
        return serializer_account_histories.data

    def get_stat(self, account):
        price_histories = PriceHistory.objects.filter(user=account.id)
        if len(price_histories) == 0:
            data = {
                'amount_price': 0,
                'avg_price': 0,
                'amount_history': 0
            }
            return data

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
