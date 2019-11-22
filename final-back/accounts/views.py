from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from .models import User
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
        
# 여기를 분리해줘야돼!! 회원가입은 따로!
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(status=400)


@api_view(['GET', 'DELETE'])
def detail(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if request.user == user:
            username = user.username
            user.delete()
            return Response({
                'message': f'유저 {username}이 정상적으로 삭제되었습니다.'
            })
    return Response(status=400)
        