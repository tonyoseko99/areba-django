# myapp urls

from django.urls import path
from myapp.views import BookList, BookDetail, home

urlpatterns = [
    path('', home, name='home'),
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),

]
