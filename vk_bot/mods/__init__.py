import pkgutil
from importlib import import_module
from vk_bot.modutil import BacisPlug
modules = []
def test(pkgname):
    global modules
    package = import_module(pkgname)
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        t = import_module(full_name)
        for name in dir(t):
            if name[0] == "_":
                continue
            atribute = t.__getattribute__(name)
            try:
                if atribute not in modules and atribute.__module__ == t.__name__:
                    if isinstance(atribute, type):
                        if issubclass(atribute, BacisPlug):
                            modules.append(atribute)
            except AttributeError:
                continue
        if is_pkg:
            test(full_name)
test(__name__)
