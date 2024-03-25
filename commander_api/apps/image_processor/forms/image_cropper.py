from django import forms
from django.utils.translation import gettext

from ..widgets.image_cropper import ImageCropperWidget


class ImageCropperForm(forms.Form):
    """Form that receives an image to have its background removed."""

    template_name = "image_processor/forms/image_cropper.html"

    image = forms.ImageField(
        label=gettext("Upload image"),
        widget=ImageCropperWidget(attrs={"class": "form-control"}),
    )
