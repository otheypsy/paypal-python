class Item:

    def __init__(self, currency):
        self.__name = 'item'
        self.__sku = "item"
        self.__price = 0
        self.__currency = currency
        self.__quantity = 1

    def name(self, name):
        self.__name = name

    def sku(self, sku):
        self.__sku = sku

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    def create_array(self):
        return {
            "name": self.__name,
            "sku": self.__sku,
            "price": self.__price,
            "currency": self.__currency,
            "quantity": self.__quantity
        }
