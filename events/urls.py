from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/events', views.EventViewSet)

urlpatterns = [
    # HTML routes
    path('', views.home, name='home'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    
    # API routes
    path('api/event/<int:event_id>/register/', views.register_for_event, name='register_api'),
] + router.urls