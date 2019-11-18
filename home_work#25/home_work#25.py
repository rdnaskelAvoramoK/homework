class Temperature:
    def celsius_kelvin(self, gradus):
        return gradus + 273.15

    def kelvin_celsius(self, gradus):
        return gradus-273.15

    def celsius_fahrenheit(self, gradus):
        return (gradus*9/5)+32

    def fahrenheit_celsius(self, gradus):
        return (gradus-32)*5/9

    def fahrenheit_kelvin(self, gradus):
        return self.celsius_kelvin(self.fahrenheit_celsius(gradus))

    def kelvin_fahrenheit(self, gradus):
        return self.celsius_fahrenheit(self.kelvin_celsius(gradus))


testTemp1 = Temperature()
print(testTemp1.kelvin_fahrenheit(100))
testTemp2 = Temperature()
print(testTemp2.fahrenheit_kelvin(800))
print(testTemp1.kelvin_celsius(273.15))
