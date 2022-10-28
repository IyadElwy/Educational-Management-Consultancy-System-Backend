from django.urls import path
from .views import Wallets, WalletDetail

urlpatterns = [
    path('', Wallets.as_view()),
    path('<int:pk>/', WalletDetail.as_view())
]
