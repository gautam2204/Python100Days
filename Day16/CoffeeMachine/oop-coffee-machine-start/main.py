from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = MenuItem()
menu.name
coffee_maker.report()
coffee_maker.is_resource_sufficient(menu.get_items())