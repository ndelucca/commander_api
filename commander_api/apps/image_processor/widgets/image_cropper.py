from .image_file_upload import ImageUploadWidget
from .utils import JSModulePath


class ImageCropperWidget(ImageUploadWidget):
    """Widget for ImageField that removes the background of an image."""

    template_name = "image_processor/widgets/image_cropper.html"

    class Media:
        css = {"all": ("css/widgets/image_cropper.css",)}
        js = (JSModulePath("js/widgets/image_cropper.js"),)
