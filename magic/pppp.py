class Iterator:
    def init(self, **kwargs):
        self.maximum = kwargs.get("maximum", 1)
        self.current = self.maximum + 1


    def iter(self):
        return self


    def next(self):
        if self.current > 1:
            self.current -= 1
            return self.current
        raise StopIteration


print(f"(Iterator){'='*40}")
instance_iterator = Iterator(maximum=5)
for item in instance_iterator:
    print(item)