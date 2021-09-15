from django.shortcuts import render, redirect
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

def show_lists(request):
  list_result_set = models.TaskList.objects.all()

  # list comprehension technique
  my_lists = [item.name for item in list_result_set]
  
  return render(request, 'todo/lists.html', {
    'lists': my_lists
  })


# CSRF: Cross Site Request Forgery
def add_list(request):
  if request.method == 'POST':
    # extract data 
    print(request.POST)
    list_name = request.POST['list_name']
    # create object and validate data (part of different functionality)
    list = models.TaskList(name=list_name)
    # save data to DB
    list.save()
    # return render(request, 'todo/lists.html')
    return redirect('lists_page')
  else:
    return render(request, 'todo/new_list.html')