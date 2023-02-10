from django.urls import path
from auth.views import MyObtainTokenPairView, RegisterView, DetailUserAPIView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UpdateProfilePictureAPIView, UserActivationAPIView, ResendActivationCodeAPIView



# from rest_framework import routers
# from django.conf.urls import include
# from django.urls import path
# from rest_framework_simplejwt.views import TokenRefreshView
# from views import (MyObtainTokenPairView, RegisterView)
#                     

urlpatterns = [
    path('auth/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('user/<int:id>/', DetailUserAPIView.as_view(), name='user_profile'),
    path('user/profile_picture/<int:id>/', UpdateProfilePictureAPIView.as_view(), name='user_picture_update'),
    path('auth/activate/<str:activation_token>/', UserActivationAPIView.as_view(), name='activate'),
    path('auth/resend-activation-code/', ResendActivationCodeAPIView.as_view(), name='resend-activation-code'),
]