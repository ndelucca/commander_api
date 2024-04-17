from datetime import datetime as dt
from typing import List, Optional

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema

from ..models import EventRecord

event_record_api = NinjaAPI()


class EventRecordError(Schema):
    message: str


class EventRecordSchema(Schema):
    id: int
    event: str
    datetime: dt


@event_record_api.get("/all", response=List[EventRecordSchema])
def get_all_event_records(request):
    return EventRecord.objects.all()


@event_record_api.get("/get/{id}", response=EventRecordSchema)
def get_event_record(request, id: int):
    event_record = get_object_or_404(EventRecord, id=id)
    return event_record


class EventRecordCreate(Schema):
    event: str
    datetime: Optional[dt] = dt.now()


@event_record_api.post("/create", response=EventRecordSchema)
def create_event_record(request, payload: EventRecordCreate):
    instance = EventRecord(
        event=payload.event,
        datetime=payload.datetime,
    )
    instance.save()
    return instance
