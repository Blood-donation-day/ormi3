from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get (self, request):
        return render(request, 'instagram/main.html')
    
    #post로 호출
    def post(self, request):
        return render(request, 'instagram/main.html')