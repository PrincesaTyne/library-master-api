from django.urls import path
from authors.views import AuthorListView, AuthorDetailView

app_name = 'authors'

urlpatterns = [
    path('', AuthorListView.as_view(), name='author-list'),
    path('<str:id>', AuthorDetailView.as_view(), name='author-detail'),
]
