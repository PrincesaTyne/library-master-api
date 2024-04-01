from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from authors.serializers import AuthorSerializer
from authors.models import Author
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


class AuthorListView(ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def list(self, request):
        authors = self.get_queryset()
        serializer = self.get_serializer(authors, many=True)
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


class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get_author(self, id):
        try:
            return Author.objects.get(pk=id)
        except Author.DoesNotExist:
            raise ValidationError({'error': 'Author does not exist'})

    def retrieve(self, request, id=None):
        author = self.get_author(id)
        serializer = self.get_serializer(author)
        return Response(
            {
                'status': 'OK',
                'data': serializer.data
            },
            status.HTTP_200_OK
        )

    def update(self, request, id=None):
        author = self.get_author(id)
        serializer = self.serializer_class(author, data=request.data, partial=True)
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
        author = self.get_author(id)
        author.delete()
        return Response(
            {
                'status': 'OK',
                'data': 'Author deleted successfully'
            },
            status.HTTP_204_NO_CONTENT
        )
