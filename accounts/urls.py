from django.urls import path
from accounts.views import UserListView, UserDetailView

app_name = 'accounts'

urlpatterns = [
  path('', UserListView.as_view(), name='user-list'),
  path('<str:id>', UserDetailView.as_view(), name='user-detail'),
]
