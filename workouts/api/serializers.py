from django.contrib.auth.models import User

from rest_framework import serializers

from workouts.models import Exercise


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Exercise
        fields = (
            'url', 'id', 'created', 'owner', 'exercise', 'gym_level',
            'equipment', 'exercise_type', 'movement_type',
            'compound_isolation', 'muscle_group', 'major_muscles',
            'minor_muscles', 'beginner', 'intermediate', 'advanced',
            'sl', 'gvt', 'main_lift'
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    exercises = serializers.HyperlinkedRelatedField(
                    many=True, view_name='exercise-detail',
                    read_only=True
                )

    class Meta:
        model = User
        fields = (
            'url', 'id', 'username', 'exercises'
        )
