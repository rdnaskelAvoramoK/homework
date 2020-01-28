class Product:
    def __init__(self, name, cost, discount=20.0):
        self.name = name
        self.cost = cost
        self.discount = discount

    def discount_off(self):
        discount = ((100 - self.discount) / 100)
        return discount

    def price_off(self):
        return self.cost


class VipProduct(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def discount_off(self):
        return 1


class Warehouse(Product):
    def __init__(self, name, cost, number=0):
        super().__init__(name, cost)
        self.__number = number

    @property
    def get_number(self):
        return self.__number

    @get_number.setter
    def get_number(self, number):
        if self.is_number(number):
            self.__number  += number

    @staticmethod
    def is_number(str):
        try:
            float(str)
            return True
        except ValueError:
            print("value is not correct")
            return False


class Bayer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    @classmethod
    def get_discount_cost(cls, prod):
        return prod.price_off()

    def calculator(self, prod):
        qnt = self.budget // self.get_discount_cost(prod)
        return qnt

    def market(self, **products):
        for key, num in products:
            try:
               if isinstance(key, Warehouse):
                   float(num)
               else:
                   print("this item is not in warehouse")
            except SyntaxError:
                print("SyntaxError in entered data")
            else:
                key.get_number = - num
                self.budget -= self.get_discount_cost(key) * num


class VipBayer(Bayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_discount_cost(cls, prod):
        return prod.discount_off() * prod.price_off()

    def calculator(self, prod):
        if isinstance(prod, VipProduct):
            return super().calculator(prod)
        qnt = self.budget // self.get_discount_cost(prod)
        return qnt


class SuperVipBuyer(VipBayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_discount_cost(cls, prod):
        return super().get_discount_cost(prod) * prod.discount_off()


bread = Product("bread", 100, 50)
milk = Product("milk", 0.82, 10)
rice = Product("rice", 3.86, 0.5)
eggs = Product("eggs", 2.27)
tomato = Product("tomato", 4.04, 12)
oranges = VipProduct("oranges", 3.99)

#print('{:.2f}'.format(bread.price_off()))

bayer1 = Bayer("Petr1", 100)
bayer2 = VipBayer("Adam", 100)
bayer3 = SuperVipBuyer("Luke", 100)

# print(bayer1.calculator(milk))
# print(bayer2.calculator(milk))
# print(bayer3.calculator(milk))

warehouse_bread = Warehouse(bread, 5)
warehouse_tomato = Warehouse(tomato, 20)

warehouse_bread.get_number = 77
print(warehouse_bread.get_number)
