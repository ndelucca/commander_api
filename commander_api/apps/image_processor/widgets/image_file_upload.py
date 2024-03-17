import uuid

from django.forms.widgets import ClearableFileInput

from .utils import JSModulePath


class ImageUploadWidget(ClearableFileInput):
    """Widget for ImageField with image preview and drag & drop functionality."""

    template_name = "image_processor/widgets/image_file_upload.html"

    class Media:
        css = {"all": ("css/widgets/image_file_upload.css",)}
        js = (JSModulePath("js/widgets/image_file_upload.js"),)

    def __init__(self, attrs=None):
        if not attrs:
            attrs = {}

        attrs["id"] = attrs.get("id", uuid.uuid4())
        attrs["class"] = attrs.get("class", "form-control")

        super().__init__(attrs)
