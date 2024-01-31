class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = ['com', 'bg', 'net', 'org']
MIN_NAME_SYMBOLS_COUNT = 4

email = input()
while email != 'End':

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(email.split('@')[0]) <= MIN_NAME_SYMBOLS_COUNT:
        raise NameTooShortError("Name must be more than 4 characters")
    elif email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")

    email = input()
