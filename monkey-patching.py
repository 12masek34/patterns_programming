def foo():
    return 1


def monkey_patch():
    return 2


foo = monkey_patch

assert foo() == 2
