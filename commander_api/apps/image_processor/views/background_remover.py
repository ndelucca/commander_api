from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from ..forms.background_remover import BackgroundRemoverForm


class BackgroundRemover(FormView):
    """Receives an image and removes the background."""

    template_name = "image_processor/views/background_remover.html"
    form_class = BackgroundRemoverForm
    success_url = reverse_lazy("images:background-remover")

    posts = ""
    unprocessed_img = None

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.unprocessed_img = request.POST.get("image")
        self.posts = request.POST
        return super().post(request, *args, **kwargs)

    def get_initial(self) -> dict:
        initial = super().get_initial()
        initial["image"] = self.unprocessed_img
        return initial

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["posts"] = self.posts
        return context

    # def render_to_json_response(self, context, **response_kwargs):
    #     """
    #     Returns a JSON response, transforming 'context' to make the payload.
    #     """
    #     return JsonResponse({"modified": "Coso"}, **response_kwargs)

    # def render_to_response(self, context):
    #     if self.submited:
    #         return self.render_to_json_response(context)
    #     else:
    #         return super().render_to_response(context)

    # def form_valid(self, form):
    #     return JsonResponse({"modified": "Coso"})
