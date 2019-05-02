from rest_framework import serializers

from workouts.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            'created', 'exercise', 'gym_level', 'equipment', 'exercise_type',
            'movement_type', 'compound_isolation', 'muscle_group', 
            'major_muscles', 'minor_muscles', 'beginner', 'intermediate',
            'advanced', 'sl', 'gvt', 'main_lift'
        )
