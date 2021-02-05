from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_desc = models.CharField(max_length=300, default="")
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, default="")
    
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


class Blogwrite(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_desc = models.CharField(max_length=300, default="")
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, default="")
        
    def __str__(self):
        return self.title