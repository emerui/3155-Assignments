import data
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients.keys():
            if ingredients[ingredient] > self.machine_resources[ingredient]:
                print("Sorry not enough", ingredient)
                return False
        return True
    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in data.recipes[sandwich_size][order_ingredients].items():
            self.machine_resources[ingredient] -= amount
        print(sandwich_size, "sandwich is ready. Bon apetit!")
