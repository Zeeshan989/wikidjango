from django.urls import path

from . import views

urlpatterns = [
    path("<str:title>", views.title, name="title"),
    path("newpage/", views.newpage, name="newpage"),
    path("", views.index, name="index"),
  
]
