class AbstractField:
    def __init__(self, *args, **kwargs):
        pass

    def is_valid(self, value):
        return bool


class TextValidator(AbstractField):
    def __init__(self, min_length=16, max_length=256, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def is_valid(self, value):
        return (len(value) >= self.min_length) and (len(value) <= self.max_length)


class IntegerValidator(AbstractField):
    def __init__(self, min_value=32, max_value=1024, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_value = min_value
        self.max_value = max_value

    def is_valid(self, value):
        return (value >= self.min_value) and (value <= self.max_value)