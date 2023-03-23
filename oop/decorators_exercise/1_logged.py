def logged(function):
    def wrapper(*args):
        nums = [str(n) for n in args]
        return f"you called {function.__name__}({', '.join(nums)})\n"\
               f"it returned {function(*args)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
