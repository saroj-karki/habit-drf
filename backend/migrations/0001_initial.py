# Generated by Django 3.1.4 on 2020-12-21 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='HabitItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.habit')),
            ],
        ),
    ]
