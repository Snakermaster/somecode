from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import  JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Snippet

from .serializers import SnippetSerializer




@api_view(['GET','POST'])
def snippet_list(request,format=None):
    """

    :param request:
    :return:
    """
    if request.method == 'GET':
    
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk,format=None):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    if request.method == 'PUT':
        # request.data可自动处理传入的json请求
        serializer = SnippetSerializer(snippet,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










