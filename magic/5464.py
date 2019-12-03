class Mainclass:
    def __new__(cls, *args, **kwargs):
        print("__new__вызван")
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print(f"__init__вызван {args} {kwargs}")

    def __del__(self):
        print("__del__вызван")


a = Mainclass(1, 2, 3, a=1, b=2)
#del a
#print(a)

class MyException(BaseException)
    pass

