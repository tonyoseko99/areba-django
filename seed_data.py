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