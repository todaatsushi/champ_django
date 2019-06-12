from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms import layout as cf


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

    goal = forms.ChoiceField(choices=GOAL_CHOICES,
                             widget=forms.RadioSelect)
    group = forms.ChoiceField(choices=MUSCLE_GROUP_CHOICES,
                              widget=forms.RadioSelect)
    cardio = forms.ChoiceField(choices=CARDIO_OPTIONS,
                               widget=forms.RadioSelect)
    gear = forms.ChoiceField(choices=EQUIPMENT_OPTIONS,
                             widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        """
        Custom layout for the form as select buttons.
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = cf.Layout(
            cf.HTML(
                """
                <h2>Step 1:</h2>
                <label class="text-muted">Chose your primary goal </label>  <br>
                <div class="step">
                    <input type="radio" name="goal" value="low" id="low">
                        <label for="low"><i class="fas fa-angle-right"></i> Strength </label><br>
                    <input type="radio" name="goal" value="mix" id="mix">
                        <label for="mix"><i class="fas fa-angle-right"></i> Muscle Growth </label><br>
                    <input type="radio" name="goal" value="high" id="high">
                        <label for="high"><i class="fas fa-angle-right"></i> Muscle Conditioning / Stamina </label><br>
                    <input type="radio" name="goal" value="cardio" id="cardio">
                        <label for="cardio"><i class="fas fa-angle-right"></i> Improve Cardio </label><br>
                </div>

                <div class="weightOptions">
                <h2>Step 2:</h2>
                <label class="text-muted">Target Body Part/Muscle Group </label>  <br>
                <div class="step">
                    <input type="radio" name="group" value="chest" id="chest">
                        <label for="chest"><i class="fas fa-angle-right"></i>  Chest</label><br>
                    <input type="radio" name="group" value="shoulders" id="shoulders">
                        <label for="shoulders"><i class="fas fa-angle-right"></i>  Shoulders</label><br>
                    <input type="radio" name="group" value="back" id="back">
                        <label for="back"><i class="fas fa-angle-right"></i>  Back </label><br>
                    <input type="radio" name="group" value="arms" id="arms">
                        <label for="arms"><i class="fas fa-angle-right"></i>  Arms</label> <br>
                    <input type="radio" name="group" value="legs" id="legs">
                        <label for="legs"><i class="fas fa-angle-right"></i>  Legs </label><br>
                    <input type="radio" name="group" value="core" id="core">
                        <label for="core"><i class="fas fa-angle-right"></i>  Core </label><br>
                    <input type="radio" name="group" value="full" id="full">
                        <label for="full"><i class="fas fa-angle-right"></i>  Full Body </label><br>
                </div>
                </div>

                <div class="cardioOptions">
                <h2>Step 2:</h2>
                <label class="text-muted">Cardio Workout Type </label>  <br/>
                <div class="step">
                    <input type="radio" name="cardio" value="hiit" id="hiit">
                        <label for="hiit"><i class="fas fa-angle-right"></i>  HIIT </label><br>
                    <input type="radio" name="cardio" value="regular" id="regular">
                        <label for="regular"><i class="fas fa-angle-right"></i>  Regular</label><br>
                    <input type="radio" name="cardio" value="both" id="both">
                        <label for="both"><i class="fas fa-angle-right"></i>  Both </label><br>
                </div>
                </div>


                <h2>Step 3:</h2>
                <label class="text-muted">Equipment & Gear</label>  <br/>
                <div class="step">
                    <input type="radio" name="gear" value="full" id="fully">
                        <label for="fully"><i class="fas fa-angle-right"></i>  Gym (Fully Equipped) </label><br>
                    <input type="radio" name="gear" value="basic" id="basic">
                        <label for="basic"><i class="fas fa-angle-right"></i>  Gym (Basic Equipment) </label><br>
                    <input type="radio" name="gear" value="gymless" id="gymless">
                        <label for="gymless"><i class="fas fa-angle-right"></i>  No Gym </label><br>
                </div>

                <div class="step">
                    <input type="submit" form="config" class="btn btn-warning disabled sub" disabled="disabled" value="Get Your Workout">
                </div>
                """
            )
        )
