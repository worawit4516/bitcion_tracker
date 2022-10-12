from django.shortcuts import render
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from historical_data.models import PriceHistory
from historical_data.serializers import PriceHistorySerializer
from wallet.models import Wallet
from wallet.serializers import WalletCreateSerializer, WalletDetailSerializer, WalletSerializer


class PriceHistoryView(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer

    def create(self, request, *args, **kwargs):
        try:
            create_data = {
                **request.data,
            }
            serializer = self.get_serializer(data=create_data)
            serializer.is_valid(raise_exception=True)
            # serializer.validated_data
            data = serializer.save()
        except Exception as e:
            return Response(data={'Response': f'save new price history failed {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        wallet = data.wallet  # serializer can access object of field that relate in own data
        wallet.balance += request.data["price"]  # When call field in request that is dict not JS
        wallet.volume += request.data["volume"]
        wallet.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            price_history = self.get_queryset().get(pk=kwargs['pk'])
            serializer = self.get_serializer(price_history)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        try:
            kwargs['partial'] = True
            # price_history = self.get_queryset().get(pk=kwargs['pk'])
            return self.update(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return Response(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

