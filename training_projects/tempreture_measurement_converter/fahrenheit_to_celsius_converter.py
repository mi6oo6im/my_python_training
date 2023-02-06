import tkinter as tk


class InvalidFahrenheitValue(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f'The value {self.f} is not a valid number in the range {self.min_f} - {self.max_f} degree'


class FahrenheitConverter:
    def __init__(self):
        self.output = None
        self.value_in_celsius = None
        self.value_in_fahrenheit = None
        self.root = tk.Tk()
        self.root.geometry('600x300')
        self.root.title('Fahrenheit to Celsius converter')
        self.label = tk.Label(self.root, text='Convert Fahrenheit degree to Celsius degree', font=('Arial', 15))
        self.label.pack(padx=20, pady=20)
        self.my_entry = tk.Entry(self.root)
        self.my_entry.pack(padx=10, pady=10)
        self.convert_button = tk.Button(self.root, text='Convert to Celsius', font=('Arial', 12),
                                        command=self.control_flow)
        self.convert_button.pack(padx=10, pady=10)
        self.textbox = tk.Text(self.root, height=3)
        self.textbox.pack(pady=10)
        self.root.configure(background='gray')
        self.root.mainloop()

    def get_entry_value(self):
        return int(self.my_entry.get())

    def pass_result(self):
        self.textbox.insert("1.0", self.output)

    def clear_textbox(self):
        self.textbox.delete("1.0", "end")

    def convert_fahrenheit_to_celsius(self):
        if InvalidFahrenheitValue.min_f <= self.value_in_fahrenheit <= InvalidFahrenheitValue.max_f:
            return (self.value_in_fahrenheit - 32) * (5 / 9)
        else:
            raise InvalidFahrenheitValue(self.value_in_fahrenheit)

    def control_flow(self):
        try:
            self.output = None
            self.value_in_fahrenheit = self.get_entry_value()
            self.value_in_celsius = self.convert_fahrenheit_to_celsius()
            self.output = f'{self.value_in_fahrenheit:.2f} degree Fahrenheit is {self.value_in_celsius:.2f} degree Celsius'
        except (InvalidFahrenheitValue, ValueError, TypeError) as err:
            self.output = err
        self.clear_textbox()
        self.pass_result()


FahrenheitConverter()
