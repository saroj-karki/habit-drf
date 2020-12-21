'''Backend views'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from . import models
from . import serializers


@api_view(['GET'])
def habits(request):
    '''Returns habit objects'''
    objects = models.Habit.objects.all()
    objects = serializers.HabitSerializer(objects, many=True)
    return Response(objects.data)


@api_view(['GET'])
def habit_details(request, primary_key):
    '''Returns habit object'''
    try:
        habit_obj = models.Habit.objects.get(id=primary_key)
    except models.Habit.DoesNotExist as exception:
        raise NotFound() from exception
    habit_obj = serializers.HabitSerializer(habit_obj)
    return Response(habit_obj.data)


@api_view(['POST'])
def habit_create(request):
    '''Creates habit object'''
    serializer = serializers.HabitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def habit_update(request, primary_key):
    '''Updates habit object'''
    try:
        habit_obj = models.Habit.objects.get(id=primary_key)
    except models.Habit.DoesNotExist as exception:
        raise NotFound() from exception
    serializer = serializers.HabitSerializer(instance=habit_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200)
    return Response(serializer.errors, status=400)
