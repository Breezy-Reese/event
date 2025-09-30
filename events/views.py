from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer

# HTML Views
def home(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'events/home.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

# API Views
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('date')
    serializer_class = EventSerializer

@api_view(['POST'])
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    # Check if event is full
    if event.registered_count >= event.max_attendees:
        return Response(
            {'error': 'This event is full'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Check if email already registered
    if Registration.objects.filter(event=event, email=request.data.get('email')).exists():
        return Response(
            {'error': 'This email is already registered for this event'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(event=event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)