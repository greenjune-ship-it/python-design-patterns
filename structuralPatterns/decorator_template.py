def my_decorator(func):
    def wrapper():
        # Do something before
        result = func
        # Do something after
        return result

    return wrapper


@my_decorator
def func():
    pass
