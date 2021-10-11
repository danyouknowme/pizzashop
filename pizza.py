"""The pizza class to using for pizza shop."""
from enum import Enum


class PizzaSize(Enum):
    """A size and price of pizza."""

    small = 120
    medium = 200
    large = 320
    jumbo = 450

    @property
    def price(self):
        """Return the price of that pizza size."""
        return self.value

    def __str__(self):
        """Return the size of pizza."""
        return self.name


class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size: PizzaSize):
        """Initialize the pizza with a size."""
        if not isinstance(size, PizzaSize):
            raise TypeError("size must be a PizzaSize")
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        price = self.size.price + 20 * len(self.toppings)
        return price

    def add_topping(self, topping):
        """Add a topping to the pizza."""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def __str__(self):
        """Return the words that describe the pizza."""
        description = str(self.size)  # or self.size.name
        if self.toppings:
            description += " pizza with " + ", ".join(self.toppings)
        else:
            description += " plain pizza"
        return description
