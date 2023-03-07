# use faker to generate fake data
import os
from myapp import views
from django.urls import path
from rest_framework import serializers
from django.db import models
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.urls import path, include
from django.contrib import admin
from faker import Faker
from myapp.models import Book
import random

fake = Faker()


def populate(N=5):
    for entry in range(N):
        # get a random date
        fake_date = fake.date()
        # get a random title
        fake_title = fake.sentence()
        # get a random author
        fake_author = fake.name()
        # create a new book entry
        book = Book.objects.get_or_create(
            title=fake_title, author=fake_author, publication_date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print("Populating Complete")

# Path: myapp/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

# Path: myapp/views.py

# Create your views here.


def home(request):
    return render(request, 'home.html')


class BookList(ListView):
    model = Book
    template_name = 'book_list.html'


class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'


# Path: myapp/models.py

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


# Path: myapp/serializers.py


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publication_date')

# Path: myapp/templates/home.html
{% extends 'base.html' % }

{% block content % }
  <h1 > Home Page < /h1 >
    <p > Click < a href = "{% url 'book_list' %}" > here < /a > to view the list of books. < /p >
{% endblock % }
# Path: myapp/templates/base.html
<!DOCTYPE html >
<html lang = "en" >
<head >

<meta charset = "UTF-8" >
  <meta name = "viewport" content = "width=device-width, initial-scale=1.0" >
   <meta http-equiv = "X-UA-Compatible" content = "ie=edge" >
    <title > Book List < /title >
</head >
<body >
    {% block content % }
    {% endblock % }
</body >
</html >
# Path: myapp/templates/book_list.html
{% extends 'base.html' % }
{% load static % }
{% block content % }
  <h1 > Book List < /h1 >
   <ul >
        {% for book in object_list % }
            <li > <a href = "{% url 'book_detail' book.id %}" > {{book.title}} < /a > </li >
        {% endfor % }
    </ul >
{% endblock % }

# Path: myapp/templates/book_detail.html
{% extends 'base.html' % }
{% load static % }
{% block content % }
  <h1 > Book Detail < /h1 >
    <p > Title: {{object.title}} < /p >
    <p > Author: {{object.author}} < /p >
    <p > Publication Date: {{object.publication_date}} < /p >
{% endblock % }
# Path: myapp/admin.py

# Register your models here.
admin.site.register(Book)

# Path: myapp/urls.py

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
]


