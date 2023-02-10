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
from ..utils import send_activation_email

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


class ResendActivationCodeAPIView(APIView):
    queryset = UserActivation.objects.all()
    serializer_class = UserActivationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        if email is None:
            return Response({'message': 'Email address is required to resend activation code.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'User with provided email address does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        if user.is_active:
            return Response({'message': 'User is already activated. No need to resend activation code.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_activation = self.queryset.get(user=user)
        except UserActivation.DoesNotExist:
            return Response({'message': 'Activation code not found for provided email address.'}, status=status.HTTP_400_BAD_REQUEST)

        activation_token = user_activation.activation_token
        # send the activation token to the user's email address
        # ...

        try:
            # send the activation email to the user
            send_activation_email(user.email, activation_token)
        except:
            return Response({'message': 'We can\'t send the activation code now. Please try latter.'}, status=status.HTTP_500_BAD_REQUEST)
            # return user

        return Response({'message': 'Activation code resent successfully to the provided email address.'})
