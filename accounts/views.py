from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        # super_user = self.request.user.is_superuser
        # users = self.get_queryset() if super_user else User.objects.filter(id=request.user.id)
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
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


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_user(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            raise ValidationError({'error': 'User does not exist'})

    def retrieve(self, request, id=None):
        user = self.get_user(id)
        serializer = self.get_serializer(user)
        return Response(
            {
                'status': 'OK',
                'data': serializer.data
            },
            status.HTTP_200_OK
        )

    def update(self, request, id=None):
        user = self.get_user(id)
        serializer = self.serializer_class(user, data=request.data, partial=True)
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
        user = self.get_user(id)
        user.delete()
        return Response(
            {
                'status': 'OK',
                'message': 'User deleted successfully'
            },
            status.HTTP_204_NO_CONTENT
        )
