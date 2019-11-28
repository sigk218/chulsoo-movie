from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movies),
    path('movies/<int:movie_pk>/', views.detail),
    path('genres/', views.genres),
    path('genres/<int:genre_pk>/', views.genre_detail),
    path('Rating/', views.rating),
    path('Rating/<int:rating_pk>/', views.rating_detail),
    path('movies/<int:movie_pk>/user/<int:user_pk>/', views.like_movie),
    path('recommendation/<int:user_pk>/', views.recommendation),
]