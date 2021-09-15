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
# create table or update table etc

# python3 manage.py migrate
# runs the script and creates the table
# run that SQL code

# TaskModel.objects.all()
# SELECT * FROM todo_task


class TaskList(models.Model):
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return self.name

class Task(models.Model):
  # fields gets mapped to columns in the table
  name = models.CharField(max_length = 50)
  desc = models.TextField()
  # the default value is set at the time class is loaded
  # created_at = models.DateTimeField(default=timezone.now())

  # function gets called to get the time when the object created
  created_at = models.DateTimeField(default=timezone.now)
  due_date = models.DateTimeField(blank=False, default=timezone.now)
  # casade deletion is where we delete the corresponding entry in task list
  # if there is no other connection to that task list
  """
  todo_task
  id                         tasklist_id
  1 scaler_task_1 ... ... ... 1
  2 scaler_task_2 ... ... ... 1

  todo_tasklist
  1 scaler
  """
  list = models.ForeignKey(TaskList, on_delete=models.CASCADE, null=True)

  def __str__(self):
      return self.name
  



