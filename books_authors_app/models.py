from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=255)
    desc= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    #RELATIONSHIP:
    #myAuthors

class Author(models.Model):
    first_name= models.CharField(max_length=45)
    last_name= models.CharField(max_length=45)
    notes= models.TextField(null=True)
    myBooks= models.ManyToManyField(Book, related_name="myAuthors")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


# Create your models here.
