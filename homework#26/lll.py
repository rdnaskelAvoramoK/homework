class A:
    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.__password = password + "1"

    @property
    def my_test(self):
        print("getter called")
        return self.__my_attr

    @my_test.setter
    def my_test(self, value):
        print("setter called")
        self.__my_attr = f"extra logic {value}"

    @my_test.deleter
    def my_test(self):
        print("deleter called")
        del self.__my_attr