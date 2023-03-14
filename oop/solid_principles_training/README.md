# SOLID Principles Training
### Judge: Not Implemented

1. Single Responsibility Principle (SRP): A class should have only one reason to change.
```# Example
class EmailSender:
    def send_email(self, email_address: str, message: str) -> None:
        # Code to send email```

2. Open/Closed Principle (OCP): A class should be open for extension but closed for modification.
3. Liskov Substitution Principle (LSP): Subtypes must be substitutable for their base types.
4. Interface Segregation Principle (ISP): A client should not be forced to depend on methods it does not use.
5. Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules. Both should depend on abstractions.

Sure! Dependency Injection is a design pattern in which the dependencies of a class or module are provided externally, rather than being created internally. The idea is to make classes more modular and independent, allowing for easier testing and flexibility.