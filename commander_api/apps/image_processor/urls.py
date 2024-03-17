from django.urls import path

from .views.background_remover import BackgroundRemover

urlpatterns = [
    path(
        "background-remover/",
        BackgroundRemover.as_view(),
        name="background-remover",
    ),
]
