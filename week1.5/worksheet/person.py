  # Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        '''creates a new person with inputted name and birthday'''
        if isinstance(name, str) == False or isinstance(birth, date) == False:
            raise TypeError
        elif name == "":
            raise ValueError
        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        '''returns the capital letters in the persons name '''
        initial = ''.join(i[0].upper for i in self.name.split() if i)
        return initial

    def is_birthday(self):
        '''returns whether or not it is the persons birthday'''
        if date.today().month == self.birth.month and date.today().day == self.birth.day:
            return True
        else:
            return False
