import datetime

import sys


class MyClass:

    def __init__(self, user_date):
        self.data = MyClass.date_converter(user_date)

    @staticmethod
    def date_converter(user_date):
        try:
            date = datetime.datetime.strptime(user_date, "%d-%m-%Y")
            return date
        except ValueError:
            sys.exit("ValueError")



cool = MyClass("8-8-1888")

print(cool.age)