"""The pizza class to using for pizza shop."""
SMALL = 'small'
MEDIUM = 'medium'
LARGE = 'large'


class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size):
        """Initialize the pizza with a size."""
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        if self.size == 'small':
            price = 120 + 20*len(self.toppings)
        elif self.size == 'medium':
            price = 200 + 20*len(self.toppings)
        elif self.size == 'large':
            price = 280 + 20*len(self.toppings)
        else:
            raise ValueError("Unknown pizza size "+self.size)
        return price

    def add_topping(self, topping):
        """Add a topping to the pizza."""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def __str__(self):
        description = self.size
        if self.toppings:
            description += " pizza with " + ", ".join(self.toppings)
        else:
            description += " plain pizza"
        return description
