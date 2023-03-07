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