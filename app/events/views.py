from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Timer, Event
from .serializers import TimerSerializer,EventSerializer

class TimerViewSet(viewsets.ModelViewSet):
    serializer_class = TimerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Timer.objects.filter(user=self.request.user).order_by('created_at')

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user).order_by('target_date')