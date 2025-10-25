from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello {request.user.username}, you are authenticated!"})

from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello {request.user.username}, you are authenticated!"})
