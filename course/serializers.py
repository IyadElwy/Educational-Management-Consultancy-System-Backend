from rest_framework import serializers
from .models import Course


class CourseSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'name',
                  'description',
                  'grade_level',
                  'school')
        model = Course

    def create(self, validated_data):
        course = Course.objects.create(name=validated_data['name'],
                                       description=validated_data['description'],
                                       grade_level=validated_data['grade_level'],
                                       school=validated_data['school'])

        return course


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',
                  'name',
                  'description',
                  'grade_level',
                  'school')
        model = Course

    def update(self, instance, validated_data):
        Course.objects.filter(id=validated_data['id']).update(name=validated_data['name'],
                                                              description=validated_data['description'],
                                                              grade_level=validated_data['grade_level'],
                                                              school=validated_data['school'])

        return Course.objects.get(id=validated_data['id'])
