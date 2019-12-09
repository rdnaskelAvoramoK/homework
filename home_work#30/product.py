class Product:
    def __init__(self, name, cost, discount = 20):
        self.name = name
        self.cost = cost
        self.discount = discount

    def get_price_off(self):
        return self.cost * self.discount_off()

    def discount_off(self):
        return (100 - self.discount)/100

class VipProduct(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def discount_off(self):
        return 1