import os

_config_name = "phonebook"
_config_exts = ["pickle", "json"]
_current_ext = "pickle"

def locate_config():
    """
    find first located config file by the list
    """
    for ext in _config_exts:
        path = _config_name + _config_exts
        if os.path.exists(path):
            _current_exts = os.path.splitext(path)[1]
            break

def create_config(extension, data):
    """
    create new config or rewite old

    @raise if extension not support
    """
    with open("file.txt", "w", errors="ignore") as f:
        if extension == "pickle":
                import serialization.pickle as pickle
                f.write(pickle.serialize(data))
        elif extension == "json":
                import serialization.json as json
                f.write(json.serialize(data))
        else
            raise KeyError("This extension of config file not supported.")

def load_config(): 
    locale_config()
    with open("file.txt", "r", errors="ignore") as f:
        if current_ext == "pickle":
            import serialization.pickle as pickle
            return pickle.deserialize(f.read())
        elif current_ext == "json":
            import serialization.json as json
            return json.deserialize(f.read())

