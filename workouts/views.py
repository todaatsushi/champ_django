from django.shortcuts import render

from workouts.forms import ConfigForm
from workouts.helpers.Workout import returnWorkout
from workouts.helpers.helper import exerciseData


def config(request):
    form_class = ConfigForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            # Get model data
            data = exerciseData()

            # Workout target
            goal = request.POST.get('goal')

            if goal == 'cardio':
                groupOrCardio = request.POST.get('cardio')

                # Jumbotron title
                spec1 = goal.capitalize()

                if groupOrCardio == 'hiit':
                    spec2 = 'HIIT'
                elif groupOrCardio == 'regular':
                    spec2 = 'regular'
                else:
                    spec2 = 'HIIT & regular'
            else:
                groupOrCardio = request.POST.get('group')

                # Jumbotron title
                spec2 = groupOrCardio

                if goal == "low":
                    spec1 = "Strength"
                elif goal == "mix":
                    spec1 = "Muscle Growth"
                else:
                    spec1 = "Muscle Conditioning"

            gear = request.POST.get('gear')

            # Configure workout object
            workout = returnWorkout(data, goal, groupOrCardio, gear)

            # Generate warmup & routine
            workout.generateWarmup()
            workout.generateRoutine()

            # Format and extract workout/routine DataFrames
            dfs = workout.formatFullRoutine()

            # Classes for table to have
            tbl_classes = ["table", "routine-custom", "table-hover",
                           "table-sm", "thead-dark"]

            # Coerce to html
            df_html = [df.to_html(
                            index=False, classes=tbl_classes,
                            justify="center"
                            ) for df in dfs]

            context = {
                'tables': df_html,
                'spec1': spec1,
                'spec2': spec2,
                'form': form,
            }

            return render(request, 'workouts/workout.html',
                          context)

    context = {
        'form': form_class
    }

    return render(request, 'workouts/config.html', context)
