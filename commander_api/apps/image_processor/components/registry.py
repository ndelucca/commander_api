class ComponentRegister:
    _registry = set()

    @classmethod
    def register(cls, obj):
        cls._registry.add(type(obj).__name__)

    @classmethod
    def display_registry(cls):
        return cls._registry


def register_obj(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        ComponentRegister.register(instance)
        return instance

    return wrapper
