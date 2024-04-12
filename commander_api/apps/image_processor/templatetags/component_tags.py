from apps.image_processor.components.registry import ComponentRegister
from django import template

register = template.Library()


@register.simple_tag()
def component_media():
    return ", ".join(ComponentRegister.display_registry())
