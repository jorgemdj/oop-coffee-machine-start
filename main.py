from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

data = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()


def machine():
    machine_on = True
    while machine_on:
        request = None
        while request is None:
            order = str(input("What would you like? (espresso/latte/cappuccino): "))
            if order == "report" or order == "off":
                request = order
            else:
                request = data.find_drink(order)

        if request == "report":
            coffee_machine.report()
            money.report()
        elif request == "off":
            machine_on = False
        else:
            if coffee_machine.is_resource_sufficient(request):
                if money.make_payment(request.cost):
                    coffee_machine.make_coffee(request)
            else:
                print("Try again later!")


machine()
