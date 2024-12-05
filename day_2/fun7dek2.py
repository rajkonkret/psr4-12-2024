def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


def bold_decorator(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        return "\033[1m" + result + "\033[0m"

    return wrapper


@bold_decorator
@uppercase_decorator
def greeting():
    return "Hello World!!!"


@bold_decorator
def greeting2(string):
    return f"Podałeś {string}"


print(greeting())  # HELLO WORLD!!!

print(greeting2("Radek"))
