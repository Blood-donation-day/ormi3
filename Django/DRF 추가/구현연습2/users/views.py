#Django Basic Modules
from django.contrib.auth import get_user_model
#Django Rest Framework
from rest_framework import generics, viewsets
from rest_framework import permissions
# local modules
from .serializers import UserSerializer

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

