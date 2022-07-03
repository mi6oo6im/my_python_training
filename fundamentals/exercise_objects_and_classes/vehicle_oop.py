class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, new_owner: str):
        if self.owner is None and money >= self.price:
            self.owner = new_owner
            change = money - self.price
            return f'Successfully bought a {self.type}. Change: {change:.2f}'
        elif self.owner is None and money < self.price:
            return "Sorry, not enough money"
        else:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        else:
            return f'{self.model} {self.type} is on sale: {self.price}'


vehicle_type = "car"
car_model = "BMW"
car_price = 30000
vehicle = Vehicle(vehicle_type, car_model, car_price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
