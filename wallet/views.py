from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import WalletSerializer_NO_ID, WalletSerializer
from .models import Wallet
from django_filters.rest_framework import DjangoFilterBackend


class Wallets(ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer_NO_ID
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['points']


class WalletDetail(RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
