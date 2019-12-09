from validators import TextValidator, IntegerValidator


class AbstractField:
    def __init__(self, validators=None, *args, **kwargs):
        pass

    def is_valid(self, value):
        pass


class CharField(AbstractField):
    def __init__(self, validators=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = [TextValidator(min_length=0, max_length=999)]
        self.all_validators = self.default
        if isinstance(validators, list) and validators:
            self.all_validators += validators

    def is_valid(self, value):
        return all(item.is_valid(value) for item in self.all_validators)


class TextField(AbstractField):
    def __init__(self, validators=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = [TextValidator(min_length=1001, max_length=3000)]
        self.all_validators = self.default
        if isinstance(validators, list) and validators:
            self.all_validators += validators

    def is_valid(self, value):
        return all(item.is_valid(value) for item in self.all_validators)




class IntegerField(AbstractField):
    def __init__(self, validators=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = [IntegerValidator(min_value=128, max_value=1024)]
        self.all_validators = self.default
        if isinstance(validators, list) and validators:
            self.all_validators += validators

    def is_valid(self, value):
        return all(item.is_valid(value) for item in self.all_validators)