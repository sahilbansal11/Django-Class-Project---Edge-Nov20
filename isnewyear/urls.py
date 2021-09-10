from django.urls import path
from isnewyear import views

urlpatterns = [
  path('', views.index)
]
