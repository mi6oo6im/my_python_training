class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, roman_value: str):
        roman_chars = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_value = roman_chars[roman_value[0]]  # get the int value of the first roman number
        for i in range(1, len(roman_value)):
            current_number = roman_chars[roman_value[i]]
            previous_number = roman_chars[roman_value[i - 1]]
            if current_number <= previous_number:
                int_value += current_number
            else:
                int_value += current_number - 2 * previous_number
        return cls(int_value)

    @classmethod
    def from_string(cls, string_value: str):
        if not isinstance(string_value, str):
            return "wrong type"
        return cls(int(string_value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
