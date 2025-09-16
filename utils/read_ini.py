import configparser
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, 'config.ini')

print(f"Trying to read config file at: {config_path}")

config = configparser.ConfigParser()
files_read = config.read(config_path)

print(f"Config files loaded: {files_read}")
print(f"Sections found: {config.sections()}")


def get_ini_data(block, key):
    try:
        return config[block][key]
    except KeyError as e:
        raise KeyError(f"Missing section/key: {e}")


print(get_ini_data('AppData', 'url'))













