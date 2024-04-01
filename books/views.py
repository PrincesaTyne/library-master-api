from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from books.serializers import BookSerializer
from books.models import Book
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


class BookListView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def list(self, request):
        # super_user = self.request.user.is_superuser
        # books = self.get_queryset() if super_user else Book.objects.filter(created_by=request.user.id)
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        return Response(
            {
                'status': 'OK',
                'data': serializer.data,
            },
            status.HTTP_200_OK
        )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status': 'OK',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)


class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_book(self, id):
        try:
            return Book.objects.get(pk=id)
        except Book.DoesNotExist:
            raise ValidationError({'error': 'Book does not exist'})

    def retrieve(self, request, id=None):
        book = self.get_book(id)
        serializer = self.get_serializer(book)
        return Response(
            {
                'status': 'OK',
                'data': serializer.data
            },
            status.HTTP_200_OK
        )

    def update(self, request, id=None):
        book = self.get_book(id)
        serializer = self.serializer_class(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'status': 'OK',
                'data': serializer.data
            },
            status.HTTP_200_OK
        )

    def destroy(self, request, id=None):
        book = self.get_book(id)
        book.delete()
        return Response(
            {
                'status': 'OK',
                'message': 'Book deleted successfully'
            },
            status.HTTP_200_OK
        )
