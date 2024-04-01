from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from genres.serializer import GenreSerializer
from genres.models import Genre
from rest_framework.response import Response
from rest_framework import status


class GenreListView(ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def list(self, request):
        # super_user = self.request.user.is_superuser
        # genres = self.get_queryset() if super_user else Genre.objects.filter(created_by=request.user.id)
        genres = self.get_queryset()
        serializer = self.get_serializer(genres, many=True)
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
        serializer.save(created_by=request.user.id)
        return Response({
            'status': 'OK',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)


class GenreDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def retrieve(self, request, id=None):
        genre = Genre.objects.get(pk=id)
        serializer = self.get_serializer(genre)
        return Response(
            {
                'status': 'OK',
                'data': serializer.data
            },
            status.HTTP_200_OK
        )

    def update(self, request, id=None):
        genre = Genre.objects.get(pk=id)
        serializer = self.serializer_class(genre, data=request.data, partial=True)
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
        genre = Genre.objects.get(pk=id)
        genre.delete()
        return Response(
            {
                'status': 'OK',
                'data': 'Genre deleted successfully'
            },
            status.HTTP_204_NO_CONTENT
        )
