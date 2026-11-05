  # Worksheet 1.5: Person class

import datetime
from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        if isinstance(name, str) == False or isinstance(birth, date) == False:
            raise TypeError
        elif name == "":
            raise ValueError
        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(name):
        return ''.join([i for i in name if i.isupper()])

    def is_birthday(birth):
        if datetime.datetime.now() == birth:
            return True
        else:
            return False
