'''Models for habit app'''
from django.db import models


class Habit(models.Model):
    '''Stores habit information'''
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class HabitItem(models.Model):
    '''Stores habit item information'''
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.habit} on {self.date.date()}'
