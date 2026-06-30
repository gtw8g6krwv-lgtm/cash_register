class ReceiptPosition:
    def __init__(self, name: str, price: int, quantity: int):
        self._name = name
        self._price = price
        self._quantity = quantity

    def increase_quantity(self, quantity_delta: int, before_negative_minimal_number = 0, in_ruble_kopecks = 100):
        if isinstance(quantity_delta, int) and quantity_delta > before_negative_minimal_number:
            self._quantity += quantity_delta
            self._price += quantity_delta * in_ruble_kopecks

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    def total_cost(self):
        return self._price * self._quantity