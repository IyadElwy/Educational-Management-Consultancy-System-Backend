from rest_framework import serializers
from .models import Application


class ApplicationSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'session',
                  'status')
        model = Application

    def create(self, validated_data):
        application = Application.objects.create(session=validated_data['session'],
                                                 status=validated_data['status'])
        return application


class ApplicationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',
                  'session',
                  'status')
        model = Application

    def update(self, instance, validated_data):
        Application.objects.filter(id=validated_data['id']).update(session=validated_data['session'],
                                                                   status=validated_data['status'])

        return Application.objects.get(id=validated_data['id'])
