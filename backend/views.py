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
