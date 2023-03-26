def type_check(type2check):
    def decorator(func):
        def wrapper(*args):
            if all([isinstance(arg, type2check) for arg in args]):
                return func(*args)

            return "Bad Type"

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

