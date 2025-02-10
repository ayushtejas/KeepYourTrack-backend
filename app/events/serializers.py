from rest_framework import serializers
from .models import Timer, Event
from django.utils import timezone

class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = ['uuid', 'title', 'created_at','duration']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)  # Remove ** as create() doesn't expect unpacked dict

class EventSerializer(serializers.ModelSerializer):
    remaining_time = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['uuid', 'title', 'target_date', 'pin', 'created_at', 'remaining_time']  # Added remaining_time

    def get_remaining_time(self, obj):
        now = timezone.now()
        if obj.target_date > now:
            return (obj.target_date - now).total_seconds()
        return 0

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)