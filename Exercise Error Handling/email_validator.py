from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


name_pattern = r"[\w+\.]+"
domain_pattern = r"\.[a-z]+"

allowed_domains = ['.com', '.bg', '.org', '.net']
email = input()

while email != "End":

    try:
        if email.count("@") > 1:
            raise MoreThanOneAtSymbolError("Email should contain only one @!")

        if len(email.split("@")[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        if '@' not in email:
            raise MustContainAtSymbolError("Email must contain @")

        if findall(name_pattern, email)[0] != email.split('@')[0]:
            raise InvalidNameError("Name cannot contain special characters")

        if findall(domain_pattern, email)[-1] not in allowed_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    except IndexError:
        print("Email is invalid!")
    else:
        print("Email is valid")

    email = input()
