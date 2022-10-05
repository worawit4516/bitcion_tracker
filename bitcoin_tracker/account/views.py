from django.shortcuts import render
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from account.models import Account
from account.serializers import AccountSerializer, AccountHistorySerializer


class AccountView(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

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
            return Response(data={'Response': f'save new user failed {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            account = self.get_queryset().get(pk=kwargs['pk'])
            serializer = AccountHistorySerializer(account)
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


