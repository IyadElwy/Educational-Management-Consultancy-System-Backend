from rest_framework import serializers
from .models import CoordinatorRating, StudentRating, MLScore


class CoordinatorRatingSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',)
        model = CoordinatorRating

    def create(self, validated_data):
        coordinator_rating = CoordinatorRating.objects.create()

        return coordinator_rating


class StudentRatingSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',)
        model = StudentRating

    def create(self, validated_data):
        student_rating = StudentRating.objects.create()

        return student_rating


class MLScoreSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',)
        model = MLScore

    def create(self, validated_data):
        ml_score = MLScore.objects.create()

        return ml_score


####################################################################################################

class CoordinatorRatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',)
        model = CoordinatorRating

    def update(self, instance, validated_data):
        CoordinatorRating.objects.filter(id=validated_data['id']).update()

        return CoordinatorRating.objects.get(id=validated_data['id'])


class StudentRatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',)
        model = StudentRating

    def update(self, instance, validated_data):
        StudentRating.objects.filter(id=validated_data['id']).update()

        return StudentRating.objects.get(id=validated_data['id'])


class MLScoreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',)
        model = MLScore

    def update(self, instance, validated_data):
        MLScore.objects.filter(id=validated_data['id']).update()

        return MLScore.objects.get(id=validated_data['id'])
