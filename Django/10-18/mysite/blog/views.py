from django.shortcuts import render
from .models import Posts
# rest_framework 추가 후 추가된 코드
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializer import PostSerializer

# FBV 사용하는 방식 

# @api_view(['GET', 'POST'])
# def postlist(request):
#     if request.method == 'GET':
#         posts = [
#             {'title':'1', 'content':'111'},
#             {'title':'2', 'content':'222'},
#             {'title':'3', 'content':'333'},
#         ]
#         serializer = posts # 직렬화 단계
#         return Response(serializer)
#     elif request.method == 'POST':
#         # POST 요청 처리
#         # ...
#         return Response({'message': 'POST 요청이 성공적으로 처리되었습니다.'}) 
#     # Response로 반환 되었을 때 데이터를 읽을 수도 있고 POST를 보낼 수도 있습니다.
    

# CBV 사용방식 

# class LicatView(APIView):
#     def get(self, request):
#         posts = [
#             {'title':'1', 'content':'111'},
#             {'title':'2', 'content':'222'},
#             {'title':'3', 'content':'333'},
#         ]
#         serializer = posts # 직렬화 하는 단계
#         return Response(serializer) # Response로 반환 되었을 때 데이터를 읽을 수도 있고, POST를 보낼 수도 있습니다.

# postlist = LicatView.as_view()


@api_view(['GET', 'POST'])
def postlist(request):
    if request.method == 'GET':
        postlist = Posts.objects.all()
        serializer = PostSerializer(postlist, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(postlist, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

