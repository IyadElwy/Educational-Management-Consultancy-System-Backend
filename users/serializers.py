from rest_framework import serializers
from .models import User,Volunteer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)


        instance.save()
        return instance

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['user', 'profle_pic', 'cv']


    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


