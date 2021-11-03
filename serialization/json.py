import json

def serialize(obj)
    """
    object to json format
    """
    return json.dumps(obj)

def deserialize(source)
    """
    deserialize json file, string, bytes etc to object
    """
    return json.load(string)
