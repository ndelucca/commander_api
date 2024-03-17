from django.urls import path

from .views.background_remover import BackgroundRemover

app_name = "image_processor"
urlpatterns = [
    path(
        "background-remover/",
        BackgroundRemover.as_view(),
        name="background-remover",
    ),
]
