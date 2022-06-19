from django.contrib import admin
from .models import Song, Type, Like

admin.site.register(Song)
admin.site.register(Type)
admin.site.register(Like)

