from .models import CustomUser
from rest_framework import generics
from .serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    """
    Create new user
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
