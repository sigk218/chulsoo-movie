from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Actor, Director, Genre, Movie, Rating
from .serializers import ActorSerializer, DirectorSerializer, GenreSerializer, MovieSerializer, RatingSerializer

# Create your views here.
@api_view(['GET', 'POST',])
def movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(status=400)