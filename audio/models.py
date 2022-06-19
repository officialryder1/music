from email.mime import image
import imp
from tkinter import CASCADE
from unicodedata import name
from urllib.parse import _NetlocResultMixinBytes
from django.db import models
from django.contrib.auth.models import User

GENRE_CHOICES = [
    ('GOSPEL','GOSPEL'),
    ('AFROBEATS', 'AFROBEATS'),
    ('RAP&HIP-HOP','RAP&HIP-HOP'),
    ('COUNTRY','COUNTRY'),
    ('POP','POP'),
    ('REGGE','REGGE'),
]
COUNTRIES = [
    ('Nigeria','Nigeria'),
    ('USA','USA'),
    ('UK','UK'),
    ('Ghana','Ghana'),
    ('Canada','Canada'),
]

class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image')
    download = models.FileField(upload_to='Music_download')
    description = models.TextField()
    genre = models.CharField(choices=GENRE_CHOICES, max_length=15)
    country = models.CharField(choices=COUNTRIES, max_length=8)
    year_release = models.DateTimeField()
    date_upload = models.DateTimeField()
    like = models.ManyToManyField(User,default=0, blank=True, related_name='song_like')

    def __str__(self):
        return self.artist +' - '+ self.title + ' - ' + self.genre

    @property
    def num_like(self):
        return self.like.all().count()

    @property
    def num_title(self):
        return self.title.all().count()
        
class Type(models.Model):
   name = models.CharField(max_length=20)
   image = models.FileField(upload_to='image')

   def __str__(self):
       return self.name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    post = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return str(self.post)
