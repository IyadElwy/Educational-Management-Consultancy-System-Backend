from rest_framework import serializers
from .models import User,Volunteer


class VolunteerSerializer(serializers.ModelSerializer):
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

        instance.is_Volunteer = True
        instance.save()
        Volunteer.objects.create(user=instance)
        return instance