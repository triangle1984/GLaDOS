import pkgutil
from importlib import import_module
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
            if atribute not in modules:
                modules.append(atribute)
        if is_pkg:
            test(full_name)
test(__name__)
