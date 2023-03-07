from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from myapp.models import Book
from myapp.serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = 'book_list.html'

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = 'book_detail.html'

def home(request):
    return render(request, 'home.html')
