from django.db import models

# Create your models here.


class Task(models.Model):
    name=models.CharField(max_length= 150)
    completed = models.BooleanField(default=False)

    # commands to run in the terminal
    #1.python manage.py makemigrations -> validates changes
    #2.python manage.py migrate -> migrates data to database