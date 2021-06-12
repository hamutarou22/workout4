from django.contrib import admin

# Register your models here.
from .models import Event, Content

admin.site.register(Event)
admin.site.register(Content)