from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Actor, Director, Genre, Movie, Rating
from .serializers import ActorSerializer, DirectorSerializer, GenreSerializer, MovieSerializer, RatingSerializer
from django.contrib.auth import get_user_model
from django.db.models import Q
# from IPython import embed


# Create your views here.
@api_view(['GET', 'POST'])
def movies(request):
    if request.method == 'GET':
        title = ''
        genres = ''
        actors = ''
        directors = ''
        for k, v in request.query_params.items():
            if k == 'title':
                title = v
            elif k == 'genres':
                genres = v
            elif k == 'actors':
                actors = v
            elif k == 'directors':
                directors = v
        actor = Actor.objects.filter(peopleNm=title)
        director = Director.objects.filter(peopleNm=title)
        genre = Genre.objects.filter(genreNm=title)
        embed()
        if actor:
            title = actor[0].id
        elif director:
            title = director[0].id
        elif genre:
            title = genre[0].id
        if genres and actors and directors:
            movies = Movie.objects.filter(title__contains=title,
                                          genres=genres,
                                          actors=actors,
                                          directors=directors
                                          )
        elif genres and actors:
            movies = Movie.objects.filter(title__contains=title,
                                          genres=genres,
                                          actors=actors
                                          )
        elif genres and directors:
            movies = Movie.objects.filter(title__contains=title,
                                          genres=genres,
                                          directors=directors
                                          )
        elif genres and actors:
            movies = Movie.objects.filter(title__contains=title,
                                          genres=genres,
                                          actors=actors
                                          )
        elif genres:
            movies = Movie.objects.filter(title__contains=title,
                                          genres=genres,
                                          )
        elif actors:
            movies = Movie.objects.filter(title__contains=title,
                                          actors=actors,
                                          )
        elif directors:
            movies = Movie.objects.filter(title__contains=title,
                                          directors=directors,
                                          )
        else:
            movies = Movie.objects.filter(Q(title__contains=title) | Q(genres=title) | Q(actors=title) | Q(directors=title))
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(status=400)


@api_view(['GET', 'DELETE',])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        title = movie.title
        movie.delete()
        return Response({
            'message': f'영화 {title}(이)가 제거 되었습니다.'
        })
    return Response(status=400)


@api_view(['GET', 'POST'])
def genres(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(status=400)

@api_view(['GET', 'DELETE',])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        genreNm = genre.genreNm
        genre.delete()
        return Response({
            'message': f'장르 {genreNm}(이)가 제거 되었습니다.'
        })
    return Response(status=400)


@api_view(['GET', 'POST',])
def rating(request):
    if request.method == 'GET':
        rating = Rating.objects.all()
        serializer = RatingSerializer(rating, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RatingSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(status=400)


@api_view(['GET', 'DELETE',])
def rating_detail(request, rating_pk):
    rating = get_object_or_404(Rating, pk=rating_pk)
    if request.method == 'GET':
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        content = rating.content
        rating.delete()
        return Response({
            'message': f'댓글 {content}(이)가 제거 되었습니다.'
        })
    return Response(status=400)


@api_view(['POST', 'DELETE'])
def like_movie(request, movie_pk, user_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(get_user_model, pk=user_pk)

    if request.method == 'POST':
        user.like_movie.add(movie)
        return Response({
            'message': f'{user.username}님 영화{movie.title} 좋아요 완료'
        })
    elif request.method == 'DELETE':
        user.like_movie.remove(movie)
        
        return Response({
            'message': f'{user.username}님 영화{movie.title} 좋아요 취소'
        })
    return Response(status=400)