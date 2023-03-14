# SOLID Principles Training
### Judge: Not Implemented

1. Single Responsibility Principle (SRP): A class should have only one reason to change.
```python
# Example
class EmailSender:
    def send_email(self, email_address: str, message: str) -> None:
        # Code to send email
```

2. Open/Closed Principle (OCP): A class should be open for extension but closed for modification.
```python
# Example
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
```
3. Liskov Substitution Principle (LSP): Subtypes must be substitutable for their base types.
```python
# Example
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(self.side, self.side)

# This violates LSP since Square cannot substitute Rectangle in all cases
def print_area(rectangle: Rectangle):
    rectangle.width = 5
    rectangle.height = 4
    assert rectangle.area() == 20
```
4. Interface Segregation Principle (ISP): A client should not be forced to depend on methods it does not use.
```python
# Example
class Bird:
    def fly(self):
        pass

    def swim(self):
        pass

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError

    def swim(self):
        # Code to swim
```
5. Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules. Both should depend on abstractions.
```python
# Example
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # Code to process payment using Stripe API

class PaymentGateway:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def process_payment(self, amount: float) -> bool:
        return self.payment_processor.process_payment(amount)
```
Dependency Injection is a design pattern in which the dependencies of a class or module are provided externally, rather than being created internally. The idea is to make classes more modular and independent, allowing for easier testing and flexibility.
