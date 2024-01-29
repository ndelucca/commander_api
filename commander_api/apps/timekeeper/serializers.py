from rest_framework import serializers

from .models.event_record import EventRecord


class EventRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRecord
        fields = ["id", "event", "datetime"]
