from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies),
    path('<int:movie_pk>/', views.detail),
]