from rest_framework import serializers
from .models import SchoolMaterial, VolunteerMaterial


class SchoolMaterialSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'session',
                  'name',
                  'description')
        model = SchoolMaterial

    def create(self, validated_data):
        school_material = SchoolMaterial.objects.create(session=validated_data['session'],
                                                        name=validated_data['name'],
                                                        description=validated_data['description'])

        return school_material


class VolunteerMaterialSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'session',
                  'name',
                  'description',
                  'is_public')
        model = VolunteerMaterial

    def create(self, validated_data):
        volunteer_material = VolunteerMaterial.objects.create(session=validated_data['session'],
                                                              name=validated_data['name'],
                                                              description=validated_data['description'],
                                                              is_public=validated_data['is_public'])

        return volunteer_material


####################################################################################################

class SchoolMaterialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',
                  'session',
                  'name',
                  'description')
        model = SchoolMaterial

    def update(self, instance, validated_data):
        SchoolMaterial.objects.filter(id=validated_data['id']).update(session=validated_data['session'],
                                                                      name=validated_data['name'],
                                                                      description=validated_data['description'])

        return SchoolMaterial.objects.get(id=validated_data['id'])


class VolunteerMaterialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',
                  'session',
                  'name',
                  'description')
        model = VolunteerMaterial

    def update(self, instance, validated_data):
        VolunteerMaterial.objects.filter(id=validated_data['id']).update(session=validated_data['session'],
                                                                         name=validated_data['name'],
                                                                         description=validated_data['description'],
                                                                         is_public=validated_data['is_public'])

        return VolunteerMaterial.objects.get(id=validated_data['id'])
