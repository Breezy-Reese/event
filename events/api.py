from rest_framework import serializers, viewsets
from .models import Event, Registration

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def api_events(request):
    events = Event.objects.all().order_by("date")
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_register(request, event_id):
    data = request.data
    data['event'] = event_id
    serializer = RegistrationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
