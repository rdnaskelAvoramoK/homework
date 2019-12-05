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

    @property
    def age(self):
        now_date = datetime.date.today().timetuple()
        birthday = self.data.timetuple()
        if now_date[0] > birthday[0]:
            if now_date[2] < birthday[2]:
                if (now_date[1] -1) < birthday[1]:
                    return (now_date[0] - birthday[0] -1)
                else:
                    return (now_date[0] - birthday[0])
            else:
                if now_date[1] < birthday[1]:
                    return (now_date[0] - birthday[0] -1)
                else:
                    return (now_date[0] - birthday[0])
        return "Указанна будущая дата"


cool = MyClass("8-8-1888")

print(cool.age)