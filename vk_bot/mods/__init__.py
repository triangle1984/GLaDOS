import pkgutil
from importlib import import_module
from vk_bot.core.modules.basicplug import BasicPlug
modules = []


def test(pkgname):
    """
    Це хоурма нужна чобы импортировать все шо есть в mods рекурсивно, ежели
    в тамошних каталогах есть пустой __init__.py
    Ее необязательно изучать или понимать, она работает довольно автономно
    и вряд ли ей когда-нибудь понадобятся изменения
    """
    # modules - список со всеми классами, наследовших BasisPlug, в данном
    # каталоге
    global modules
    package = import_module(pkgname)
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        # фулл нейм, пример: mods.games.smeh
        full_name = package.__name__ + '.' + name
        # импорт этого самого фулл нейма в переменную
        t = import_module(full_name)
        # скипать все атрибуты модуля, с _ в начале названия
        for name in dir(t):
            if name[0] == "_":
                continue
            # записать атрибут в переменную
            atribute = t.__getattribute__(name)
            try:
                # ежели атрибут уже не сохранен, а так ежели он относится к
                # модулю, а не чота левое и импортированное, например сторонние
                # либы
                if atribute not in modules and atribute.__module__ == t.__name__:
                    # это класс
                    if isinstance(atribute, type):
                        # этот класс наследует BasicPlug
                        if issubclass(atribute, BasicPlug):
                            # сохранить его в список модулей
                            modules.append(atribute)
            except AttributeError:
                continue
        # Ежели это каталог, то так же пройтись по всем файлам в том каталоге
        if is_pkg:
            test(full_name)


test(__name__)
