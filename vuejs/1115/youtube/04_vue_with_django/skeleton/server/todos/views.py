from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == 'GET':
        
        #todos = Todo.objects.all()
        #요청 유저의 todo만 역참조로 불러온다
        todos = request.user.todo_set.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 토큰 정보가 추가되고 있지 않으므로 토큰 정보를 추가해 준다. 
            # 즉 유저 정보를 추가해준다.
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)

    if not request.user.todo_set.filter(pk=todo_pk).exists():
        return Response({'detil' : '권한이 없습니다.'}, status = status.HTTP_403_FORMIDDON)

    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        todo.delete()
        return Response({ 'id': todo_pk }, status=status.HTTP_204_NO_CONTENT)
