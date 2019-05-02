from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from workouts.models import Exercise
from workouts.serializers import ExerciseSerializer


@csrf_exempt
def exercise_list(request):
    """
    List all exercises / create new exercise entry.
    """

    if request.method == 'GET':
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExerciseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def exercise_detail(request, pk):
    """
    Retrieve, update or delete an exercise entry.
    """
    try:
        exercise = Exercise.objects.get(pk=pk)
    except Exercise.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExerciseSerializer(exercise)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExerciseSerializer(exercise, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        exercise.delete()
        return HttpResponse(status=204)
