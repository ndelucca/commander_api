from drf_spectacular.utils import extend_schema
from rest_framework import generics

from ..models import EventRecord
from ..serializers import EventRecordSerializer


@extend_schema(
    summary="Retrieve an EventRecord",
    description="This endpoint retrieves an EventRecord by its id.",
)
class EventRecordDetailView(generics.RetrieveAPIView):
    queryset = EventRecord.objects.all()
    serializer_class = EventRecordSerializer
    lookup_field = "id"
