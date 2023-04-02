from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    order_id = 1

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    @property
    def valid_meal_types(self):
        return {
            "Starter": Starter,
            "MainDish": MainDish,
            "Dessert": Dessert,
        }

    def register_client(self, client_phone_number: str):
        same_number_clients = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if same_number_clients:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if not isinstance(meal, Starter) and not isinstance(meal, MainDish) and not isinstance(meal, Dessert):
                continue

            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join(m.details() for m in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        # check if the client is registered if not register the client
        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        # check if the meal names from the order are available on the menu
        meal_names_on_menu = [m.name for m in self.menu]
        meal_names_and_qty_from_order = dict(meal_names_and_quantities)
        meal_names_not_on_menu = [m for m in meal_names_and_qty_from_order if m not in meal_names_on_menu]
        if meal_names_not_on_menu:
            raise Exception(f"{meal_names_not_on_menu[0]} is not on the menu!")

        meals_to_order = [m for meal in meal_names_and_qty_from_order for m in self.menu if m.name == meal]
        ordered_meals = [self.valid_meal_types[m.__class__.__name__](m.name, m.price, meal_names_and_qty_from_order[m.name])
                         for m in meals_to_order]

        meals_with_insufficient_quantity = [m for m in meals_to_order if m.quantity < meal_names_and_qty_from_order[m.name]] # next(filter(lambda m: m.quantity < meal_names_and_qty_from_order[m.name], meals_to_order))
        if meals_with_insufficient_quantity:
            raise Exception(f"Not enough quantity of {meals_with_insufficient_quantity[0].__class__.name}: {meals_with_insufficient_quantity[0].name}!")
        client.shopping_cart.extend(ordered_meals)
        for meal in ordered_meals:
            meal_quantity = meal.quantity
            meal.quantity -= meal_quantity
            client.bill += meal_quantity * meal.price
        meal_names_only_string = ', '.join(m.name for m in client.shopping_cart)
        return f"Client {client.phone_number} successfully ordered {meal_names_only_string} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            self.menu[meal.name] += meal.quantity

        client.shopping_cart.clear()
        client.bill = 0
        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        receipt_id = FoodOrdersApp.order_id
        total_paid_money = client.bill
        client.shopping_cart.clear()
        client.bill = 0.0
        FoodOrdersApp.order_id += 1

        return f"Receipt #{receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client.phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
