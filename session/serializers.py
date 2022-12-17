from rest_framework import serializers
from .models import Session


class SessionSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'course',
                  'description',
                  'start_time',
                  'end_time',
                  )
        model = Session

    def create(self, validated_data):
        session = Session.objects.create(course=validated_data['course'],
                                         description=validated_data['description'],
                                         start_time=validated_data['start_time'],
                                         end_time=validated_data['end_time'], )

        return session


class SessionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',
                  'course',
                  'description',
                  'start_time',
                  'end_time',
                  )
        model = Session

    def update(self, instance, validated_data):
        Session.objects.filter(id=validated_data['id']).update(course=validated_data['course'],
                                                               description=validated_data['description'],
                                                               start_time=validated_data['start_time'],
                                                               end_time=validated_data['end_time'], )

        return Session.objects.get(id=validated_data['id'])
