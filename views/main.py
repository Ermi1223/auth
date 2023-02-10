from ..serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from ..models import Profile
from ..serializers import RegisterSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


from ..serializers import (
    RegisterSerializer,
    UserDetailSerializer,
    ProfilePictureSerializer,
)

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
)


from rest_framework.permissions import (
    AllowAny,
    # IsOwner,
)
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.generics import (
    UpdateAPIView,
)
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class UpdateProfilePictureAPIView(UpdateAPIView):
    queryset = Profile.objects.all()
    lookup_field = "id"
    serializer_class = ProfilePictureSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return self.request.user.profile

    def update(self, request, *args, **kwargs):
        profile_picture = self.request.FILES.get('profile_picture')
        if profile_picture:
            self.get_object().profile_picture = profile_picture
            self.get_object().save()
        return super().update(request, *args, **kwargs)


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

