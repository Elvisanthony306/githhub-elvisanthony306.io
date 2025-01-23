from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.contrib.auth.models import BaseUserManager
# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_id = models.IntegerField(null=True, blank=True, unique=True)
    city = models.CharField(max_length=80)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} UserProfile"



@receiver(post_save, sender=User, dispatch_uid="create_profile")
def create_user_profile(sender, created, instance, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=500, null=False, blank=False)
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} post {self.id}"
