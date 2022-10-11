from rest_framework import serializers
from wallet.models import Wallet
from historical_data.models import PriceHistory
from account.models import Account
from historical_data.serializers import PriceHistorySerializer
from django.db.models import OuterRef, Subquery, Sum

import json


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = (
            'wallet_id',
            'user',
            'link_account',
            'balance',
            'volume'
        )


class WalletCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = (
            'wallet_id',
            'user',
            'link_account'
        )


class WalletDetailSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    volume = serializers.SerializerMethodField()
    link_account = serializers.SerializerMethodField()

    class Meta:
        model = Wallet
        fields = (
            'wallet_id',
            'user',
            'balance',
            'volume',
            'link_account'
        )

    def get_balance(self, wallet):
        price_histories = PriceHistory.objects.filter(user=wallet.user)
        balance = 0
        for history in price_histories:
            balance += history.price
        return balance

    def get_volume(self, wallet):
        price_histories = PriceHistory.objects.filter(user=wallet.user)
        balance = 0
        for history in price_histories:
            balance += history.volume
        return balance

    def get_link_account(self, wallet):
        link_account = json.loads(wallet.link_account)
        data = []
        for accounts in link_account:
            account = Account.objects.get(pk=accounts)
            data.append({
                'id': account.id,
                'email': account.email,
            })
        return data
