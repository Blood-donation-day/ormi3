from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fileds = '__all__'