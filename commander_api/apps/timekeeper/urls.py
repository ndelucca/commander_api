from django.urls import path

from .views.crud import EventRecordDetailView

urlpatterns = [
    path(
        "eventrecord/<int:id>/",
        EventRecordDetailView.as_view(),
        name="eventrecord-detail",
    ),
]
