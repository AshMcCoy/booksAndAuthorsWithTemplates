from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('createBook', views.createBook, name= 'createBook'),
    path('createAuthor', views.createAuthor, name= 'createAuthor'),
    path('newAuthor', views.newAuthor, name= 'newAuthor'),
    path('addAuthor', views.addAuthor, name='addAuthor'),
    path('addBook', views.addBook, name='addBook'),
    path('book/<int:bookId>', views.showBook, name= 'showBook'),
    path('author/<int:authorId>', views.showAuthor, name='showAuthor'),
]