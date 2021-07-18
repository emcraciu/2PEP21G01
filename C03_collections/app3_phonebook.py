""" Create a self ordering phonebook
    - add numbers
    - remove numbers
"""
from collections import OrderedDict


class PhoneBook:

    def __init__(self):
        self.phonebook = OrderedDict()

    def add_number(self, name, number):
        self.phonebook[name] = number
        for key in self.phonebook.copy().keys():
            if key > name:
                self.phonebook.move_to_end(key)

    def remove_number(self, name=None, number=None):
        if name:
            self.phonebook.pop(name)
        elif number:
            for key, value in self.phonebook.copy().items():
                if value == number:
                    self.phonebook.pop(key)


if __name__ == '__main__':
    phonebook = PhoneBook()
    phonebook.add_number("Maria", "0720543505")
    phonebook.add_number("Ion", "0725543505")
    phonebook.add_number("Aon", "0725543505")
    phonebook.add_number("Bon", "0725543505")
    phonebook.add_number("Zon", "0725543505")
    phonebook.add_number("Fon", "0725543506")
    phonebook.remove_number(name='Bon')
    phonebook.remove_number(number='0725543506')

    print(phonebook.phonebook.items())
