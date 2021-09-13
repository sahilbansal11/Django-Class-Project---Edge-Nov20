from django.db import models
from django.utils import timezone

# Create your models here.

# ORM
# Object Relational Mapper (ORM)
# Object reminds you of classes
# Relational => DBMS
# Connect these 2 things together, Python class map to a table in DB


# Changes -> Migrations

# python3 manage.py makemigrations
# It is creating a script for me
# which will map this model class to a table in the DB
# create the necessary SQL code

# python3 manage.py migrate
# runs the script and creates the table
# run that SQL code

# TaskModel.objects.all()
# SELECT * FROM todo_task

class Task(models.Model):
  # fields gets mapped to columns in the table
  name = models.CharField(max_length = 50)
  desc = models.TextField()
  # the default value is set at the time class is loaded
  # created_at = models.DateTimeField(default=timezone.now())

  # function gets called to get the time when the object created
  created_at = models.DateTimeField(default=timezone.now)
