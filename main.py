import keyboard
import pkgutil
import importlib
import pkgutil

def main():
    clear_defined_hotkeys()
    register_all()
    while True:
        pass

def register_all():
    # hardcoded for now
    package_name = 'modules'

    module_names = [name for _, name, _ in pkgutil.iter_modules([package_name])]

    for module_name in module_names:
        register_from_module_name(package_name + '.' + module_name)

def register_from_module_name(module_name):
    module = importlib.import_module(module_name)
    # todo error checking
    print('registering: ' + module.shortcut)
    return keyboard.add_hotkey(module.shortcut, module.action)

def clear_defined_hotkeys():
    try:
        keyboard.unhook_all_hotkeys()
    except AttributeError:
        pass

if __name__ == "__main__":
    main()