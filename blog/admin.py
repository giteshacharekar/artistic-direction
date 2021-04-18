from django.contrib import admin 
from blog.models import Post, ArtComment

admin.site.register((Post, ArtComment))