class Transaction:

    def __init__(self, currency):
        self.__item_list = []
        self.__total = 0
        self.__currency = currency
        self.__description = ''

    def item_list(self, item_list):
        for item in item_list:
            self.__item_list.append(item.create_array())
            self.__total += float(item.price)

    def create_array(self):
        return {
            "item_list": {
                "items": self.__item_list
            },
            "amount": {
                "total": self.__total,
                "currency": "USD"},
            "description": self.__description
        }
