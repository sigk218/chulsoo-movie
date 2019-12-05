from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Actor, Director, Genre, Movie, Rating
from .serializers import ActorSerializer, DirectorSerializer, GenreSerializer, MovieSerializer, RatingSerializer
from django.contrib.auth import get_user_model
from rest_framework import pagination, generics

# Create your views here.
@api_view(['GET', 'POST'])
def movies(request):
    if request.method == 'GET':
        title = ''
        genres = ''
        actors = ''
        directors = ''
        actor = ''
        director = ''
        genre = ''
        actorid = 0
        directorid = 0
        genreid = 0
        for k, v in request.query_params.items():
            if k == 'title':
                title = v
            elif k == 'genres':
                genres = v
            elif k == 'actors':
                actors = v
            elif k == 'directors':
                directors = v
        if title:
            actor = Actor.objects.filter(peopleNm=title)
            director = Director.objects.filter(peopleNm=title)
            genre = Genre.objects.filter(genreNm=title)

        if actor:
            actorid = actor[0].id
        elif director:
            directorid = director[0].id
        elif genre:
            genreid = genre[0].id

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
            movies = Movie.objects.filter(title__contains=title)

        if actorid:
            movies = Movie.objects.filter(actors=actorid)
        elif genreid:
            movies = Movie.objects.filter(genres=genreid)
        elif directorid:
            movies = Movie.objects.filter(directors=directorid)
        
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(status=400)

class MoviePagination(pagination.PageNumberPagination):
    page_size = 20  # the no. of company objects you want to send in one go

# Assume url for this view is /api/v1/movies/
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination

@api_view(['GET', 'DELETE', 'PUT'])
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
    elif request.method == 'PUT':
        # 업데이트할 때 영화정보 웬만하면 다 넣어주자.
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

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


@api_view(['POST'])
def like_movie(request, movie_pk, user_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'POST':
        if not user.like_movie.filter(pk=movie_pk):
            user.like_movie.add(movie)
            return Response({
                'message': f'{user.username}님 영화{movie.title} 좋아요 완료'
            })
        else:
            user.like_movie.remove(movie)
            return Response({
                'message': f'{user.username}님 영화{movie.title} 좋아요 취소'
            })
    return Response(status=400)

@api_view(['GET'])
def recommendation(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    rcmnd = {}
    like_movies = user.like_movie.all()
    for movie in like_movies:
        # embed()
        for genre in movie.genres.all():
            g_movies = Movie.objects.filter(genres=genre.id)
            for g_movie in g_movies:
                if rcmnd.get(g_movie.id):
                    rcmnd[g_movie.id] += 2
                else:
                    rcmnd[g_movie.id] = 2
        for actor in movie.actors.all():
            a_movies = Movie.objects.filter(actors=actor.id)
            for a_movie in a_movies:
                if rcmnd.get(a_movie.id):
                    rcmnd[a_movie.id] += 1
                else:
                    rcmnd[a_movie.id] = 1
        for director in movie.directors.all():
            d_movies = Movie.objects.filter(directors=director.id)
            for d_movie in d_movies:
                if rcmnd.get(d_movie.id):
                    rcmnd[d_movie.id] += 3
                else:
                    rcmnd[d_movie.id] = 3
    rcmnd = sorted(rcmnd.items(), key=lambda x: x[1], reverse=True)
    rcccd = []
    for movieid in rcmnd:
        if not user.like_movie.filter(pk=movieid[0]):
            rcccd.append(movieid[0])

    return Response(rcccd)