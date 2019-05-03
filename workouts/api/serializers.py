from django.contrib.auth.models import User

from rest_framework import serializers

from workouts.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Exercise
        fields = (
            'id', 'created', 'owner', 'exercise', 'gym_level',
            'equipment', 'exercise_type', 'movement_type',
            'compound_isolation', 'muscle_group', 'major_muscles',
            'minor_muscles', 'beginner', 'intermediate', 'advanced',
            'sl', 'gvt', 'main_lift'
        )


class UserSerializer(serializers.ModelSerializer):
    exercises = serializers.PrimaryKeyRelatedField(
                    many=True, queryset=Exercise.objects.all()
                )

    class Meta:
        model = User
        fields = (
            'id', 'username', 'exercises'
        )
