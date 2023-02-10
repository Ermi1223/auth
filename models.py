from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        app_label = 'auth'


class UserActivation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_token = models.CharField(max_length=100, unique=True)
    
    class Meta:
        app_label = 'auth'
