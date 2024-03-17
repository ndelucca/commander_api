import base64

from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from PIL import Image
from rembg import remove

from ..forms.background_remover import BackgroundRemoverForm


class BackgroundRemover(FormView):
    """Receives an image and removes the background."""

    template_name = "image_processor/views/background_remover.html"
    form_class = BackgroundRemoverForm
    success_url = reverse_lazy("images:background-remover")

    def form_valid(self, form: BackgroundRemoverForm) -> HttpResponse:
        unprocessed_img = form.cleaned_data["image"]

        with unprocessed_img.open("rb") as img_file:
            img_bytes = img_file.read()

        base64_img = base64.b64encode(remove(img_bytes))  # type: ignore
        base64_img_str = f"data:image/png;base64,{base64_img.decode('utf-8')}"

        return JsonResponse({"image_file": base64_img_str})
