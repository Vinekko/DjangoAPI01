from django.urls import path
from .views import booksAPIView

urlpatterns = [
    path('', booksAPIView.as_view(), name='book_list'),
]