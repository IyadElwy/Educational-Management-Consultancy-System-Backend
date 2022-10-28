from rest_framework import serializers
from .models import Wallet


class WalletSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'points')
        model = Wallet

    def create(self, validated_data):
        wallet = Wallet.objects.create(points=validated_data['points'])

        return wallet


class WalletSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',
                  'points')
        model = Wallet

    def update(self, instance, validated_data):
        Wallet.objects.filter(id=validated_data['id']).update(points=validated_data['points'])

        return Wallet.objects.get(id=validated_data['id'])
