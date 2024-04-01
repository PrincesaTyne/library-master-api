from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from borrowings.serializers import BorrowingSerializer
from borrowings.models import Borrowing
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


class BorrowingListView(ListCreateAPIView):
    serializer_class = BorrowingSerializer
    queryset = Borrowing.objects.all()

    def list(self, request):
        borrowings = self.get_queryset()
        serializer = self.get_serializer(borrowings, many=True)
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


class BorrowingDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BorrowingSerializer
    queryset = Borrowing.objects.all()

    def get_borrowing(self, id):
        try:
            return Borrowing.objects.get(pk=id)
        except Borrowing.DoesNotExist:
            raise ValidationError({'error': 'Borrowing does not exist'})

    def retrieve(self, request, id=None):
        borrowing = self.get_borrowing(id)
        serializer = self.get_serializer(borrowing)
        return Response(
            {
                'status': 'OK',
                'data': serializer.data
            },
            status.HTTP_200_OK
        )

    def update(self, request, id=None):
        borrowing = self.get_borrowing(id)
        serializer = self.serializer_class(borrowing, data=request.data, partial=True)
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
        borrowing = self.get_borrowing(id)
        borrowing.delete()
        return Response(
            {
                'status': 'OK',
                'data': 'Borrowing deleted successfully'
            },
            status.HTTP_204_NO_CONTENT
        )
