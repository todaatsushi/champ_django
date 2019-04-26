from django import forms


class ConfigForm(forms.Form):
    GOAL_CHOICES = (
        ('low', 'Strength'),
        ('mix', 'Muscle Growth'),
        ('high', 'Muscle Conditioning / Stamina'),
        ('cardio', 'Improve Cardio'),
    )

    MUSCLE_GROUP_CHOICES = (
        ('chest', 'Chest'),
        ('shoulders', 'Shoulders'),
        ('back', 'Back'),
        ('arms', 'Arms'),
        ('legs', 'Legs'),
        ('core', 'Core'),
        ('full', 'Full Body'),
    )

    CARDIO_OPTIONS = (
        ('hiit', 'HIIT'),
        ('regular', 'Regular'),
        ('both', 'Both')
    )

    EQUIPMENT_OPTIONS = (
        ('full', 'Gym (Fully Equipped)'),
        ('basic', 'Gym (Basic Equipment)'),
        ('gymless', 'No Gym')
    )

    goal = forms.ChoiceField(choices=GOAL_CHOICES)
    group = forms.ChoiceField(choices=MUSCLE_GROUP_CHOICES)
    cardio = forms.ChoiceField(choices=CARDIO_OPTIONS)
    gear = forms.ChoiceField(choices=EQUIPMENT_OPTIONS)


class ContactForm(forms.Form):
    pass
