from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  print("in the index method")
  return HttpResponse("Hello World!")

# /hello/sahil
# /hello/nirmal
def greet(request, name):
  print("in the greet method")
  # return HttpResponse(f"Hello {name.capitalize()}")
  # render the hello.html template as the response for this request
  # with the context or data as {'user_name': name}
  return render(request, "hello.html", {'user_name': name.capitalize()})


