from django.urls import path

from .views.background_remover import BackgroundRemover
from .views.image_cropper import ImageCropper

app_name = "image_processor"
urlpatterns = [
    path(
        "background-remover/",
        BackgroundRemover.as_view(),
        name="background-remover",
    ),
    path(
        "image-cropper/",
        ImageCropper.as_view(),
        name="image-cropper",
    ),
]
