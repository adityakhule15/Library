from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.BooksList.postSave, name="postSave"),
        path('listOfBooks/', views.BooksList.ListOfBooks, name="listOfBooks"),
        path('update/', views.BooksList.update, name="update"),
        path('delete/', views.BooksList.delete, name="delete"),
    ]