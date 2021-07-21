_contact_book = {}

def if_exist(f):
    """
    decoractor - check if name exist

    @raise if not exist
    """
    def wrapper(name):
        if name not in _contact_book:
            raise KeyError("Contact not exist")
        return f(name)
    return wrapper

def if_not_exist(f):
    """
    decoractor - check if name exist

    @raise if not exist
    """
    def wrapper(name, phone):
        if name in _contact_book:
            raise KeyError("Contact already exist")
        return f(name, phone)
    return wrapper
            
@if_not_exist
def add(name, phone):
    """
    add contact to dictionary
    add(name, phone)
    """
    _contact_book[name] = phone

@if_exist
def get(name):
    """ get contact phone """
    return _contact_book[name]

@if_exist
def update(name, phone):
    """ update(name, phone) """
    _contact_book.update({name: phone})

def list():
    """
    list()
    @return copy of contact_book
    """
    return _contact_book.copy()

@if_exist
def delete(name):
    """ delete(name) """
    _contact_book.pop(name)

