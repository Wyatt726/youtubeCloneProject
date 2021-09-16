import re
from warnings import showwarning
from django.db.models import manager
from django.http.response import Http404
from django.shortcuts import render
import rest_framework
from .models import Video
from .serializers import VideoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.
class VideoList(APIView):

    def get(self, request):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDetail(APIView):

    def  get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = VideoSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = VideoSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)