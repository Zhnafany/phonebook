import functools

_contact_book = {}

def expect_name(condition):
    """
    decoractor - check if name exist or not depends on condition

    @raise if exist or not
    """
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args):
            name = args[0]
            if name not in _contact_book and condition:
                raise KeyError("Contact not exist")
            if name in _contact_book and not condition:
                raise KeyError("Contact already exist")
            return f(*args)
        return wrapper
    return decorator
            
@expect_name(False)
def add(name, phone):
    """
    add contact to dictionary
    add(name, phone)
    """
    _contact_book[name] = phone

@expect_name(True)
def get(name):
    """ get contact phone """
    return _contact_book[name]

@expect_name(True)
def update(name, phone):
    """ update(name, phone) """
    _contact_book.update({name: phone})

def list():
    """
    list()
    @return copy of contact_book
    """
    return _contact_book.copy()

@expect_name(True)
def delete(name):
    """ delete(name) """
    _contact_book.pop(name)
