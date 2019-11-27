from django.urls import path
from . import views

urlpatterns = [
    path('', views.users),
    path('<int:user_pk>/', views.detail),
    path('<int:follower_pk>/follow/<int:following_pk>/', views.follow),
]