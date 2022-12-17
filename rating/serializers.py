from rest_framework import serializers
from .models import CoordinatorRating, StudentRating, MLScore


class CoordinatorRatingSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'session',
                  'question_1',
                  'question_2',
                  'question_3',
                  'question_4',
                  'question_5',
                  'question_6',
                  )
        model = CoordinatorRating

    def create(self, validated_data):
        coordinator_rating = CoordinatorRating.objects.create(session=validated_data['session'],
                                                              question_1=validated_data['question_1'],
                                                              question_2=validated_data['question_2'],
                                                              question_3=validated_data['question_3'],
                                                              question_4=validated_data['question_4'],
                                                              question_5=validated_data['question_5'],
                                                              question_6=validated_data['question_6'],
                                                              )

        return coordinator_rating


class StudentRatingSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'session',
                  'question_1',
                  'question_2',
                  'question_3',
                  'question_4',
                  'question_5',
                  'question_6',
                  'question_7',
                  'question_8',
                  'question_9',
                  'question_10',
                  'question_11',
                  )

        model = StudentRating

    def create(self, validated_data):
        student_rating = StudentRating.objects.create(
            session=validated_data['session'],
            question_1=validated_data['question_1'],
            question_2=validated_data['question_2'],
            question_3=validated_data['question_3'],
            question_4=validated_data['question_4'],
            question_5=validated_data['question_5'],
            question_6=validated_data['question_6'],
            question_7=validated_data['question_7'],
            question_8=validated_data['question_8'],
            question_9=validated_data['question_9'],
            question_10=validated_data['question_10'],
            question_11=validated_data['question_11'],
        )

        return student_rating


class MLScoreSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'percentage', 'session')
        model = MLScore

    def create(self, validated_data):
        ml_score = MLScore.objects.create(percentage=validated_data['percentage'])

        return ml_score


####################################################################################################

class CoordinatorRatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',
                  'session',
                  'question_1',
                  'question_2',
                  'question_3',
                  'question_4',
                  'question_5',
                  'question_6',
                  )
        model = CoordinatorRating

    def update(self, instance, validated_data):
        CoordinatorRating.objects.filter(id=validated_data['id']).update(session=validated_data['session'],
                                                                         question_1=validated_data['question_1'],
                                                                         question_2=validated_data['question_2'],
                                                                         question_3=validated_data['question_3'],
                                                                         question_4=validated_data['question_4'],
                                                                         question_5=validated_data['question_5'],
                                                                         question_6=validated_data['question_6'])

        return CoordinatorRating.objects.get(id=validated_data['id'])


class StudentRatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',
                  'session',
                  'question_1',
                  'question_2',
                  'question_3',
                  'question_4',
                  'question_5',
                  'question_6',
                  'question_7',
                  'question_8',
                  'question_9',
                  'question_10',
                  'question_11',
                  )
        model = StudentRating

    def update(self, instance, validated_data):
        StudentRating.objects.filter(id=validated_data['id']).update(
            session=validated_data['session'],
            question_1=validated_data['question_1 '],
            question_2=validated_data['question_2 '],
            question_3=validated_data['question_3 '],
            question_4=validated_data['question_4 '],
            question_5=validated_data['question_5 '],
            question_6=validated_data['question_6 '],
            question_7=validated_data['question_7 '],
            question_8=validated_data['question_8 '],
            question_9=validated_data['question_9 '],
            question_10=validated_data['question_10'],
            question_11=validated_data['question_11'],
        )

        return StudentRating.objects.get(id=validated_data['id'])


class MLScoreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id', 'percentage')
        model = MLScore

    def update(self, instance, validated_data):
        MLScore.objects.filter(id=validated_data['id']).update(percentage=validated_data['percentage'])

        return MLScore.objects.get(id=validated_data['id'])
