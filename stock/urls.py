
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
]
