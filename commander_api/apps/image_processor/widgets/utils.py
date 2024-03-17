from django.templatetags.static import static
from django.utils.html import html_safe


@html_safe
class JSModulePath:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f'<script type="module" src="{static(self.path)}"></script>'
