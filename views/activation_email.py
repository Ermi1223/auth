from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from ..utils import send_activation_email, generate_token
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from ..models import UserActivation
from ..serializers import UserActivationSerializer

class UserActivationAPIView(APIView):
    queryset = UserActivation.objects.all()
    serializer_class = UserActivationSerializer
    permission_classes = [AllowAny]

    def get(self, request, activation_token, *args, **kwargs):
        try:
            user_activation = self.queryset.get(activation_token=activation_token)
            user = user_activation.user
        except UserActivation.DoesNotExist:
            return Response({'message': 'Activation link is invalid or has already been used.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user.is_active = True
        user.save()
        user_activation.delete()
        
        return Response({'message': 'User activation successful. You can now log in to the system.'})
