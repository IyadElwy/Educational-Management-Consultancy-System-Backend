from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import WalletSerializer_NO_ID, WalletSerializer
from .models import Wallet


class Wallets(ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer_NO_ID


class WalletDetail(RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
