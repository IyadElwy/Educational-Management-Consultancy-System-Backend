from rest_framework import serializers
from .models import SchoolMaterial


class SchoolMaterialSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'course',
                  'name',)
        model = SchoolMaterial

    def create(self, validated_data):
        school_material = SchoolMaterial.objects.create(course=validated_data['course'],
                                                        name=validated_data['name'],
                                                        )

        return school_material


####################################################################################################

class SchoolMaterialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',
                  'course',
                  'name',)
        model = SchoolMaterial

    def update(self, instance, validated_data):
        SchoolMaterial.objects.filter(id=validated_data['id']).update(course=validated_data['course'],
                                                                      name=validated_data['name'],
                                                                      )

        return SchoolMaterial.objects.get(id=validated_data['id'])
