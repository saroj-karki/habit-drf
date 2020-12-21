'''Serializer classes'''
from rest_framework.serializers import ModelSerializer

from . import models


class HabitSerializer(ModelSerializer):
    '''HabitSerializer class'''
    class Meta:
        model = models.Habit
        fields = '__all__'


class HabitItemSerializer(ModelSerializer):
    '''HabitItemSerializer class'''
    class Meta:
        model = models.HabitItem
        fields = '__all__'
