import uuid

from django.forms.widgets import ClearableFileInput


class ImageBackgroundRemoverWidget(ClearableFileInput):
    """Widget for ImageField that removes the background of an image."""

    template_name = "image_processor/widgets/image_background_remover.html"

    class Media:
        css = {"all": ("css/widgets/image_background_remover.css",)}
        js = ("js/widgets/image_background_remover.js",)

    def __init__(self, attrs=None):
        if not attrs:
            attrs = {}

        attrs["id"] = attrs.get("id", uuid.uuid4())
        attrs["class"] = attrs.get("class", "form-control")

        super().__init__(attrs)
