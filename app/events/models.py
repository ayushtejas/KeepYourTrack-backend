from django.db import models
from core.models import User
import uuid

class Timer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(default=True, blank=True, max_length=200)
    duration = models.BigIntegerField(default=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Event(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(default=True, blank=True, max_length=200)
    target_date = models.DateTimeField()
    pin = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
