from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from ..utils import send_activation_email, generate_token
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

class ActivateView(APIView):
    def get(self, request, activation_token, *args, **kwargs):
        try:
            user = User.objects.get(activation_token=make_password(activation_token))
        except User.DoesNotExist:
            return Response({'message': 'Activation link is invalid or has already been used.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user.is_active = True
        user.activation_token = ''
        user.save()
        
        return Response({'message': 'User activation successful. You can now log in to the system.'})
