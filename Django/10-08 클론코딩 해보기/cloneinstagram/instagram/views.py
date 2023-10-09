from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed
from rest_framework.response import Response
import os
from .settings import MEDIA_ROOT
from uuid import uuid4
from datetime import datetime
from user.models import User

class Main(APIView):
    def get (self, request):
        feed_list = Feed.objects.all().order_by('-id') # select * from content_feed / 아이디 인덱스의 역순으로
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()

        if email is None:
            print('얘 이메일 없음. 로그인으로 보낼게.')
            return render(request, "user/login.html")
        if user is None:
            return render(request, "user/login.html")

        #로그
        print('로그인한 사용자: ' + request.session['email'])

        return render(request, 'instagram/main.html', context=dict(feed_list=feed_list))

class UploadFeed(APIView):

# 올라온 파일은 uuid로 특정 id값을 만들어 저장
# media는 사용자가 올리는 파일들을 관리하는 곳
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

#파일을 제외한 데이터 가져오기
        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')

        Feed.objects.create(
            content = content, 
            image = image, 
            profile_image = profile_image,
            user_id = user_id,
            like_count = 0
            )
        
        return Response(status = 200) #굿