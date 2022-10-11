from rest_framework import serializers
from historical_data.models import PriceHistory

import json


class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = (
            'date',
            'price',
            'volume',
            'user',
            'wallet'
        )
