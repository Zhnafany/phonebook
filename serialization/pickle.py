import pickle

def serialize(obj):
    """
    obj to pickle serialized data
    """
    return pickle.dumps(obj)

def deserialize(string):
    """
    deserialize file, string, bytes etc to object
    """
    return pickle.loads(string)
