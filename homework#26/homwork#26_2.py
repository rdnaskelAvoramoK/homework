class readCSV:
    def __init__(self, text):
        self.name = text

    def __iter__(self):
        with open(self.name) as f:
            for line in f:
                print("|".join(line.split(",")))

test = readCSV("./convertcsv.csv")

