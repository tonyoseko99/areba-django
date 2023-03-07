# create views for the home page, book list, and book detail

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from myapp.models import Book

# home
def home(request):
    return render(request, 'base.html')

# BookList
def BookList(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# BookDetail
def BookDetail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book_detail.html', {'book': book})
