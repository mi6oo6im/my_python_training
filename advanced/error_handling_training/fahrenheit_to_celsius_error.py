class InvalidFahrenheitValue(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f'The value {self.f} is not a valid number in the range {self.min_f} - {self.max_f} degree'


def convert_fahrenheit_to_celsius(value):
    if InvalidFahrenheitValue.min_f <= value <= InvalidFahrenheitValue.max_f:
        return (value - 32) * (5 / 9)
    else:
        raise InvalidFahrenheitValue(value)


try:
    value_in_fahrenheit = int(input('Please input Fahrenheit degree value: '))
    value_in_celsius = convert_fahrenheit_to_celsius(value_in_fahrenheit)
    print(f'{value_in_fahrenheit:.2f} degree Fahrenheit is {value_in_celsius:.2f} degree Celsius')
except (InvalidFahrenheitValue, ValueError, TypeError) as err:
    print(err)
