import importlib
import pkgutil

import handlers


def load_handlers(app):
    for module_info in pkgutil.iter_modules(handlers.__path__):
        module = importlib.import_module(
            f"handlers.{module_info.name}"
        )

        register = getattr(module, "register", None)

        if register:
            register(app)
