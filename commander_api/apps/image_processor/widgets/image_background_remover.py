from .image_file_upload import ImageUploadWidget
from .utils import JSModulePath


class ImageBackgroundRemoverWidget(ImageUploadWidget):
    """Widget for ImageField that removes the background of an image."""

    template_name = "image_processor/widgets/image_background_remover.html"

    class Media:
        css = {"all": ("css/widgets/image_background_remover.css",)}
        js = (JSModulePath("js/widgets/image_background_remover.js"),)
