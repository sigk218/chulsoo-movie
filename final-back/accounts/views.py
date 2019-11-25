from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from .models import User
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.core import serializers

# Create your views here.
@require_http_methods(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = serializers.serialize('json', users)
        return JsonResponse(serializer, safe=False)
# 여기를 분리해줘야돼!! 회원가입은 따로!
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            serializers = serializers.serialize('json', form)
            return JsonResponse(serializer, safe=False)
    return JsonResponse({
        'message': 400
    })

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



        