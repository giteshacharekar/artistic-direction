from django.contrib import admin
from .models import Contact, artlike

# Register your models here.
admin.site.register((Contact, artlike))
