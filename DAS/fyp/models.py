from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    short_desc = models.CharField(max_length=300, default="")
    slug = models.SlugField(max_length=25)
    time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, default="")
    username = models.CharField(max_length=20, default="")
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class E_Awareness(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(null=True)

    def __str__(self):
        return self.title


class F_Awareness(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(null=True)

    def __str__(self):
        return self.title


#class Profile(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#    bio = models.TextField(max_length=500, blank=True)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200,default="")
    files = models.FileField()
#upload_to='media', default='media/avatar.png'

    def __str__(self):
        return self.user.username
    