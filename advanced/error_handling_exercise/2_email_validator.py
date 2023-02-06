import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def email_validator(email, regex, domain_names):
    matches = re.findall(pattern, current_email)
    try:
        if '@' not in email:
            raise MustContainAtSymbolError('Email must contain @')  # error handling - no @ character
        elif len(matches[0][0]) <= 4:
            raise NameTooShortError(
                'Name must be more than 4 characters')  # error handling - name is shorter than 4 characters
        elif matches[0][2] not in domain_names:
            raise InvalidDomainError(
                'Domain must be one of the following: .com, .bg, .org, .net')  # error handling - domain is not in domain list
        else:
            return 'Email is valid'
    except IndexError:  # any invalid character in email
        return 'Invalid Email'


domains = ['.com', '.bg', '.org', '.net']
pattern = r"([\.\w]+)@([a-z]+)(\.[a-z]+)"
current_email = input()
while not current_email == 'End':
    print(email_validator(current_email, pattern, domains))
    current_email = input()
