from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Homepage - list events
def home(request):
    events = Event.objects.all()
    return render(request, "events/home.html", {"events": events})

# Event detail
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "events/detail.html", {"event": event})

# Registration form
def register(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        Registration.objects.create(event=event, name=name, email=email)
        return redirect("home")
    return render(request, "events/register.html", {"event": event})


# ---------------- API ---------------- #

def api_events(request):
    events = list(Event.objects.values())
    return JsonResponse(events, safe=False)

@csrf_exempt
def api_register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        event = get_object_or_404(Event, id=data["event_id"])
        reg = Registration.objects.create(event=event, name=data["name"], email=data["email"])
        return JsonResponse({"status": "success", "id": reg.id})
    return JsonResponse({"error": "POST required"}, status=400)
