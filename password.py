import getpass
from typing import  Protocol



class FilterProtocol(Protocol):
    def validate(self, password: str) -> list:
        raise NotImplemented(" Filter must have implemented validate function")

class LenghtFilter(FilterProtocol):
    def __init__(self, min: int= 4, max: int = None):
        self.min = min
        self.max = max

    def validate(self, password: str) -> list:
        errors = []
        if len(password) < self.min:
            errors.append(f'Password Lenght is smaller than min({self.min})!')
        if self.max is not None and len(password) > self.max:
            errors.append(f'Password Lenght is bigger than max({self.max})!')
        return errors

class SpecialCharFilter():
    def __init__(self,special_chars= [".",",","*"], min = 1):
        self.special_chars = special_chars
        self.min = min
    def validate(self, password: str) -> list:
        errors = []
        special_chars = 0
        for char in self.special_chars:
            if char in password:
                special_chars += 1
            if special_chars < self.min:
                errors.append('Password must contain at least one special character')
            return errors

class AndFilter(FilterProtocol):

    def __init__(self, filters: list):
        self.filters = filters

    def validate(self, password: str) -> list:
        errors = []
        for filter in self.filters:
            _error: list = filter.validate(password)
            errors += _error
        return errors


if __name__ == '__main__':
    password = getpass.getpass("Check: ")
    filters = []
    special_char_filter = SpecialCharFilter()
    filters.append(special_char_filter)
    lenght = LenghtFilter(8)
    filters.append(lenght)
    and_filter = AndFilter(filters)
    while True:
     password = getpass.getpass("Check: ")
     errors = and_filter.validate(password)
     if len(errors) == 0:
         print("Password is ok")
     else:
         print("Password error:")
         for error in errors:
            print(" \t-", error)