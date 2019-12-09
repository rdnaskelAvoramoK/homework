from product import Product, VipProduct

class Warehouse:
    def __init__(self, prod, quantity):
        self.prod = prod.name
        self.__quantity = quantity

    @property
    def storekeeper(self):
        print("getter called")
        return self.__quantity

    @storekeeper.setter
    def storekeeper(self, value):
        print("setter called")
        self.__quantity = f"extra logic {value}"

    @storekeeper.deleter
    def storekeeper(self):
        print("deleter called")
        del self.__quantity


class Buyer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def quantity_of_goods(self, prod):
        quantity = str(self.budget // prod.get_price_off())
        name = prod.name
        return (self.name + " can buy " + quantity + " " + name)


class VIP_Buyer(Buyer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__discount = 0.8

    def get_discount(self):
        return self.__discount

    def quantity_of_goods(self, prod):
        if isinstance(prod, VipProduct):
            return super().quantity_of_goods(prod)
        else:
            quantity = str(self.budget // (self.get_discount()*prod.get_price_off()))
            name = prod.name
            return (self.name + " can buy " + quantity + " " + name)


class SuperVIP_Buyer(VIP_Buyer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__discount = 0.8

    def get_discount(self):
        return super().get_discount() * self.__discount



p1 = Product(name='milk', cost=1000)
p2 = Product("cheese", 7000, 50)
p3 = VipProduct("caviar", 777)

# print(p1.get_price_off(), " = ", p1.discount_off())
# print(p2.get_price_off(), " = ", p2.discount_off())
# print(p3.get_price_off(), " = ", p3.discount_off())

user1 = Buyer("Ivan", 10000.0)
user2 = VIP_Buyer("Petr", 10000.0)
user3 = SuperVIP_Buyer("Tom", 10000.0)

# print(user1.quantity_of_goods(p1))
# print(user2.quantity_of_goods(p1))
# print(user3.quantity_of_goods(p1))
#
# print(user1.quantity_of_goods(p2))
# print(user2.quantity_of_goods(p2))
# print(user3.quantity_of_goods(p2))
#
# print(user1.quantity_of_goods(p3))
# print(user2.quantity_of_goods(p3))
# print(user3.quantity_of_goods(p3))