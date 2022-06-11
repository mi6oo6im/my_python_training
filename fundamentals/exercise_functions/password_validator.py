def characters_length(password: str):
    if 6 <= len(password) <= 10:
        return True
    else:
        print("Password must be between 6 and 10 characters")
        return False


def letters_and_digits(password: str):
    if password.isalnum():
        return True
    else:
        print("Password must consist only of letters and digits")
        return False


def at_least_two_digits(password: str):
    numbers_counters = 0
    for i in password:
        if i.isnumeric():
            numbers_counters += 1
    if numbers_counters >= 2:
        return True
    else:
        print("Password must have at least 2 digits")
        return False


def password_validation(password: str):
    validation = [characters_length(password),
                  letters_and_digits(password),
                  at_least_two_digits(password)]
    if all(validation):
        print("Password is valid")


password = input()
password_validation(password)
