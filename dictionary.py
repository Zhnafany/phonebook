_contact_book = {}

def add(name, phone):
    """
    add contact to dictionary
    add(name, phone)

    @raise if contact already exist
    """
    if not exist(name):
        _contact_book[name] = phone
    else:
        raise KeyError("Contact already exist")

def exist(name):
    """
    check if contact exist with such name
    """
    return name in _contact_book

def get(name):
    """
    get contact phone

    @raise if contact not exist
    """
    if exist(name):
        return _contact_book[name]
    else:
        raise KeyError("Contact not exist")

def update(name, phone):
    """
    update(name, phone)

    @raise if not exist
    """
    if exist(name):
        _contact_book.update({name: phone})
    else:
        raise KeyError("Contact not exist")

def list():
    """
    list()
    @return copy of contact_book
    """
    return _contact_book.copy()

def delete(name):
    """
    delete(name)

    @raise if contact not exist
    """
    if exist(name):
        _contact_book.pop(name)
    else:
        raise KeyError("Contact not exist")

