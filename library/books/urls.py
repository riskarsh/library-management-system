from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("create/", views.create, name="book_create"),
    path("<int:book_id>/update", views.update, name="book_update"),
    path("<int:book_id>/delete", views.delete, name="book_delete"),
    path("", views.list, name="book_list"),
]
