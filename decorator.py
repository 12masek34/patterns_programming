# decorator pattern


def decorator(func):
    def wrapper():
        result = func()
        return f'Result {result}'

    return wrapper


@decorator
def foo():
    return 'hello'


print(foo())


###################################################

# decorator with arg

def decorator(row_return: bool):
    def decorator_(func):
        def wrapper():
            result = func()

            if row_return:
                return result

            return f'Result {result}'

        return wrapper

    return decorator_


@decorator(row_return=True)
def foo():
    return 'hello'


print(foo())
