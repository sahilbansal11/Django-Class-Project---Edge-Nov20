from django.urls import path
from hello import views

urlpatterns = [
  path('', views.index),
  path('<str:name>/', views.greet)
]

# project urls.py where we included hello.urls