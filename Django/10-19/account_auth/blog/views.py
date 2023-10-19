from django.shortcuts import render
from .models import Post

# rest_framework 추가 후 추가된 코드
from .serializers import PostSerializer #serializers.py에서 설정
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated



# @api_view(['GET', 'POST'])
# def postlist(request):
#     if request.method == 'GET':
#         post_list = Post.objects.all()
#         serializer = PostSerializer(post_list, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class PostListAPIView(APIView):
#     def get(self, request):
#         post_list = Post.objects.all()
#         serializer = PostSerializer(post_list, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# postlist = PostListAPIView.as_view()




class PostListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        post_list = Post.objects.all()
        serializer = PostSerializer(post_list, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
postlist = PostListAPIView.as_view()