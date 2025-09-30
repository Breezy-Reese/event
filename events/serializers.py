from rest_framework import serializers
from .models import Event, Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'name', 'email', 'registered_at']

class EventSerializer(serializers.ModelSerializer):
    registrations = RegistrationSerializer(many=True, read_only=True)
    is_upcoming = serializers.ReadOnlyField()
    registered_count = serializers.ReadOnlyField()
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 
                 'max_attendees', 'is_upcoming', 'registered_count', 'registrations']