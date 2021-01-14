from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search1/", views.search1, name="search1"),
    path("wiki/"+"<str:name>", views.entry, name="entry")
]
