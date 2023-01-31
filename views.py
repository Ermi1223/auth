from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics

from .serializers import (
    RegisterSerializer,
    UserDetailSerializer,
)

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
)


from rest_framework.permissions import (
    AllowAny,
    # IsOwner,
)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class DetailUserAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the details of a user instance. Searches user using id field.

    put:
        Updates an existing user. Returns updated user data

        parameters: [id, title, body, description, image]

    delete:
        Delete an existing user

        parameters = [id]
    """

    queryset = User.objects.all()
    lookup_field = "id"
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny] #[IsOwner]

