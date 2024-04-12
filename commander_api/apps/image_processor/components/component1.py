from apps.image_processor.components.registry import register_obj


@register_obj
class Component1:
    def __init__(self, name):
        self.name = name
