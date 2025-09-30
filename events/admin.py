from django.contrib import admin
from .models import Event, Registration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'registered_count', 'max_attendees', 'is_upcoming']
    list_filter = ['date', 'location']
    search_fields = ['title', 'description']

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'event', 'registered_at']
    list_filter = ['event', 'registered_at']
    search_fields = ['name', 'email']