from django import forms
from django.utils.translation import gettext

from ..widgets.image_background_remover import ImageBackgroundRemoverWidget


class BackgroundRemoverForm(forms.Form):
    """Form that receives an image to have its background removed."""

    template_name = "image_processor/forms/background_remover.html"

    image = forms.ImageField(
        label=gettext("Upload image"),
        widget=ImageBackgroundRemoverWidget(attrs={"class": "form-control"}),
    )
