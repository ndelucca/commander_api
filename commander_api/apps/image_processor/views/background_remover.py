from django.urls import reverse_lazy
from django.views.generic import FormView

from ..forms.background_remover import BackgroundRemoverForm


class BackgroundRemover(FormView):
    """Receives an image and removes the background."""

    template_name = "image_processor/views/background_remover.html"
    form_class = BackgroundRemoverForm
    success_url = reverse_lazy("images:background-remover")
