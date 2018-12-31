from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    #additional classes
    portfolio_site = models.URLField(blank=True) #user dont have to fill this Field
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)#where to upload users pics, also dont have to be filled

    def __str__(self):
        return self.user.username #user is defaul attribute of User
