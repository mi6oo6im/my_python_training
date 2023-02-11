########################################################################################################################
#                                                                                                                      #
#                            _____                                   _                                                 #
#                           |_   _|__ _ __ ___  _ __   ___ _ __ __ _| |_ _   _ _ __ ___                                #
#                             | |/ _ \ '_ ` _ \| '_ \ / _ \ '__/ _` | __| | | | '__/ _ \                               #
#                             | |  __/ | | | | | |_) |  __/ | | (_| | |_| |_| | | |  __/                               #
#                             |_|\___|_| |_| |_| .__/ \___|_|  \__,_|\__|\__,_|_|  \___|                               #
#                                              |_|                                                                     #
#                                                                                                                      #
########################################################################################################################

import tkinter as tk
import pytemp as pt


# QA:
# print('Kelvin to Fahrenheit', pt.pytemp(12, 'k', 'f'))
# print('Fahrenheit to Kelvin', pt.pytemp(12, 'f', 'k'))
# print('Celsius to Fahrenheit', pt.pytemp(12, 'c', 'f'))
# print('Fahrenheit to Celsius', pt.pytemp(12, 'f', 'c'))
# print('Celsius to Kelvin', pt.pytemp(12, 'c', 'k'))
# print('Kelvin to Celsius', pt.pytemp(12, 'k', 'c'))


def select_all(event):
    event.widget.selection_range(0, 'end')
    return 'break'


class FahrenheitConverter:
    def __init__(self):
        self.convert_from = None
        self.convert_to = None
        self.output = None
        self.value_converted = None
        self.value_to_convert = None
        self.root = tk.Tk()
        self.root.geometry('600x300')
        self.root.title('Temperature metrics converter')
        self.label = tk.Label(self.root, text='Temperature Scale Converter', font=('Arial', 17))
        self.label.pack(padx=20, pady=20)

        self.my_entry = tk.Entry(self.root, font=('Arial', 15), justify='center')
        self.my_entry.insert(0, "Enter value to convert")
        self.my_entry.pack(padx=10, pady=10)
        self.my_entry.bind('<FocusIn>', select_all)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)

        self.btn1 = tk.Button(self.button_frame, text='°F => °C', font=('Arial', 12), command=self.convert_fahr_to_cel)
        self.btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.btn2 = tk.Button(self.button_frame, text='°C => °F', font=('Arial', 12), command=self.convert_cel_to_fahr)
        self.btn2.grid(row=1, column=0, sticky=tk.W + tk.E)

        self.btn3 = tk.Button(self.button_frame, text='K => °C', font=('Arial', 12), command=self.convert_kel_to_cel)
        self.btn3.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.btn4 = tk.Button(self.button_frame, text='°C => K', font=('Arial', 12), command=self.convert_cel_to_kel)
        self.btn4.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.btn5 = tk.Button(self.button_frame, text='°F => K', font=('Arial', 12), command=self.convert_fahr_to_kel)
        self.btn5.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.btn6 = tk.Button(self.button_frame, text='K => °F', font=('Arial', 12), command=self.convert_kel_to_fahr)
        self.btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

        self.button_frame.pack(fill='x')
        self.textbox = tk.Text(self.root, height=3, font=('Arial', 12), state='disabled')
        self.textbox.pack(pady=10)
        self.root.configure(background='light gray')
        self.root.mainloop()

    def get_entry_value(self):
        return int(self.my_entry.get())

    def pass_result(self):
        self.textbox.config(state='normal')
        self.clear_textbox()
        self.textbox.insert("1.0", self.output)
        self.textbox.config(state='disabled')

    def clear_textbox(self):
        self.textbox.delete("1.0", "end")

    def converter(self, convert_from, convert_to):
        try:
            self.output = None
            self.value_to_convert = self.get_entry_value()
            self.value_converted = pt.pytemp(self.value_to_convert, convert_from, convert_to)
            self.convert_from = 'degree Fahrenheit'
            self.convert_to = 'degree Celsius'
            self.control_flow()
        except ValueError:

            self.output = 'Please enter a valid value to convert'
            self.pass_result()

    def convert_fahr_to_cel(self):
        self.converter('f', 'c')

    def convert_cel_to_fahr(self):
        self.converter('c', 'f')

    def convert_kel_to_cel(self):
        self.converter('k', 'c')

    def convert_cel_to_kel(self):
        self.converter('c', 'k')

    def convert_fahr_to_kel(self):
        self.converter('f', 'k')

    def convert_kel_to_fahr(self):
        self.converter('k', 'f')

    def control_flow(self):
        self.output = f'{self.value_to_convert:.2f} {self.convert_from} is {self.value_converted:.2f} {self.convert_to}'
        self.pass_result()


FahrenheitConverter()
