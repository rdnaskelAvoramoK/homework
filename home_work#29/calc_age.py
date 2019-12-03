import datetime


class MyClass:

    def __init__(self, user_date):
        self.data = self.date_converter(user_date)

    def date_converter(self, data):
        return self.validate(data)

    def validate(self, data):
        try:
            date = datetime.datetime.strptime(data, "%d-%m-%Y")
        except ValueError:
            print("Could not convert data to date.")
        else:
            return date

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
        else:
            return "date of birth is not correct"

cool = MyClass("11-10-1980")

print(cool.age())