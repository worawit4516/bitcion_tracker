from django.shortcuts import render
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from wallet.models import Wallet
from wallet.serializers import WalletCreateSerializer, WalletDetailSerializer


class WalletView(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    queryset = Wallet.objects.all()
    action_serializers = {
        'create': WalletCreateSerializer,
        'partial_update': WalletDetailSerializer,
        'retrieve': WalletDetailSerializer,
        'list': WalletDetailSerializer
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super().get_serializer_class()

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
            return Response(data={'Response': f'save new wallet failed {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            wallet = self.get_queryset().get(pk=kwargs['pk'])
            serializer = self.get_serializer(Wallet)
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

