import keyboard
import pkgutil
import importlib
import pkgutil
import logging
import logging.config
import sys
import yaml
import configparser

log = logging.getLogger()

def read_config(config_file_path):
    with open(config_file_path) as config_file:
        config = yaml.full_load(config_file)
    return config

def setup_logging():
    logging.config.fileConfig('./config/logging.conf')

def main():
    setup_logging()

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
    log.debug('registering: ' + module.shortcut)
    return keyboard.add_hotkey(module.shortcut, module.action)

def clear_defined_hotkeys():
    try:
        keyboard.unhook_all_hotkeys()
    except AttributeError:
        pass

if __name__ == "__main__":
    main()
