from django.urls import path

from .api.event_record import event_record_api

urlpatterns = [
    path("event_record/", event_record_api.urls),
]
