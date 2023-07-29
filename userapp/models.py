from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)#on_delete=models.CASCADE=>if user will delete account profile will delete
    image=models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location=models.CharField( max_length=100)

    def __str__(self):
        return self.user.username 

