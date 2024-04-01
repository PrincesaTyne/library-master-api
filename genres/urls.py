from django.urls import path
from genres.views import GenreListView, GenreDetailView

app_name = 'genres'

urlpatterns = [
  path('', GenreListView.as_view(), name='genre-list'),
  path('<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),
]
