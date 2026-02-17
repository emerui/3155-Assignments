import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        print("Hello, what sandwich would you like? (Large, Medium, Small, off , Report)")
        n = input().lower().strip()
        if n == "report":
            for resource in sandwich_maker_instance.machine_resources:
                if resource == "cheese":
                    print("There are ", sandwich_maker_instance.machine_resources[resource], "cheese pound(s) left")
                    continue
                print("There are ", sandwich_maker_instance.machine_resources[resource], " ", resource, " slice(s) left")
            continue
        if n == "off":
            break
        if n not in ["large", "medium", "small"]:
            print("not an option")
            continue
        cost = recipes.get(n).get("cost")
        if n == "large":
            if sandwich_maker_instance.check_resources(recipes.get("large").get("ingredients")):
                print("You owe", cost)
                if not cashier_instance.transaction_result(cost, cashier_instance.process_coins()):
                    continue
                else:
                    sandwich_maker_instance.make_sandwich(n, "ingredients")

        if n == "medium":
            if sandwich_maker_instance.check_resources(recipes.get("medium").get("ingredients")):
                print("You owe", cost)
                if not cashier_instance.transaction_result(cost, cashier_instance.process_coins()):
                    continue
                else:
                    sandwich_maker_instance.make_sandwich(n, "ingredients")

        if n == "small":
            if sandwich_maker_instance.check_resources(recipes.get("small").get("ingredients")):
                print("You owe", cost)
                if not cashier_instance.transaction_result(cost, cashier_instance.process_coins()):
                    continue
                else:
                    sandwich_maker_instance.make_sandwich(n, "ingredients")
if __name__=="__main__":
    main()
