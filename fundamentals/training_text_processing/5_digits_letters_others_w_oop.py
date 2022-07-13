class Classifier:
    def __init__(self, input_str: str):
        self.input_str = input_str

    def numbers_method(self):
        return ''.join([x for x in self.input_str if x.isdigit()])

    def letters_method(self):
        return ''.join([x for x in self.input_str if x.isalpha()])

    def symbols_method(self):
        return ''.join([x for x in self.input_str if not x.isalnum()])

    def __repr__(self):
        res = self.numbers_method()
        res += f'\n{self.letters_method()}'
        res += f'\n{self.symbols_method()}'
        return res


classifier = Classifier(input())
print(classifier)
