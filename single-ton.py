class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance





a = Singleton()
b = Singleton()

print(id(a))
print(id(b))
print(a is b)
print(a == b)
