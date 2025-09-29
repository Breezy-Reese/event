from django.urls import path
from . import views
from . import api
urlpatterns = [
    path("", views.home, name="home"),
    path("event/<int:event_id>/", views.event_detail, name="event_detail"),
    path("event/<int:event_id>/register/", views.register, name="register"),

    # APIs
    path("api/events/", views.api_events, name="api_events"),
    path("api/register/", views.api_register, name="api_register"),
]
