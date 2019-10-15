import importlib, pkgutil
modules = []
package = importlib.import_module(__name__)
for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
    full_name = package.__name__ + '.' + name
    modules.append(importlib.import_module(full_name))
