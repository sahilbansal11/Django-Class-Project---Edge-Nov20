from django.shortcuts import render

# Create your views here.

my_todos = [
  'write script to automate a random thing',
  'fix a bug on production',
  'teach django models'
]

def index(request):
  return render(request, 'todos.html', {
    'tasks': my_todos
  })