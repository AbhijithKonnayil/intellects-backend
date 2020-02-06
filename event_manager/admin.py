from django.contrib import admin
from .models import Event, EventTag

admin.site.register(EventTag)
admin.site.register(Event)
