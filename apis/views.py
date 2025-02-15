from rest_framework import generics
from library.models import Books
from apis.serializers import BookSerializer

# Create your views here.

class booksAPIView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
