from django.urls import path

from . import views

urlpatterns = [
    path("<str:title>", views.title, name="title"),
    path("newpage/", views.newpage, name="newpage"),
    path("randpage/", views.randpage, name="randpage"),
    path("", views.index, name="index"),
    path("<str:title>/editpage/", views.editpage, name="editpage"),

]
