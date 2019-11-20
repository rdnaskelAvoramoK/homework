class Temperature:
    def celsius_kelvin(self, gradus):
        return gradus + 273.15

    def kelvin_celsius(self, gradus):
        return gradus - 273.15

    def celsius_fahrenheit(self, gradus):
        return (gradus * 9 / 5) + 32

    def fahrenheit_celsius(self, gradus):
        return (gradus - 32) * 5/9

    def fahrenheit_kelvin(self, gradus):
        return self.celsius_kelvin(self.fahrenheit_celsius(gradus))

    def kelvin_fahrenheit(self, gradus):
        return self.celsius_fahrenheit(self.kelvin_celsius(gradus))

    def calculation(self, inputData):
        data = inputData.split()
        rezult = []
        for el in data:
            if el[-2:].upper() == "*K":
                rezult.append(round(self.kelvin_celsius(int(el[:-2])), 2))
            elif el[-2:].upper() == "*F":
                rezult.append(round(self.fahrenheit_celsius(int(el[:-2])), 2))
            elif el[-2:].upper() == "*C":
                rezult.append(round(int(el[:-2]), 2))
        MaxT = data[(rezult.index(max(rezult)))]
        MinT = data[(rezult.index(min(rezult)))]
        average = round(sum(rezult)/len(rezult), 1)
        print('average temperature is', average)
        return [data, rezult, (max(rezult), min(rezult)), (MaxT, MinT), average]



testTemp1 = Temperature()
print(testTemp1.kelvin_fahrenheit(100))
testTemp2 = Temperature()
print(testTemp2.fahrenheit_kelvin(800))
print(testTemp1.kelvin_celsius(273.15))
print(testTemp1.calculation("18*C 87*F 300*K 65*C 255*F"))