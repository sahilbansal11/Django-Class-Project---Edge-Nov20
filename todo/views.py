from django.shortcuts import render
from . import models
# Create your views here.

# my_todos = [
#   'write script to automate a random thing',
#   'fix a bug on production',
#   'teach django models'
# ]

def index(request):
  # list of query set
  # SELECT * FROM todo_task
  todo_result_set = models.Task.objects.all()

  # list comprehension technique
  my_todos = [[item.name, item.desc] for item in todo_result_set]
  print(my_todos)
  return render(request, 'todos.html', {
    'tasks': my_todos
  })

