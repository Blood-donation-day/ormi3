from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get (self, request):
        feed_list = Feed.objects.all().order_by('-id') # select * from content_feed / 아이디 인덱스의 역순으로
    
        return render(request, 'instagram/main.html', context=dict(feed_list=feed_list))

# Create your views here.

