class Classifier:
    def __init__(self, input_str: str):
        self.input_str = input_str

    def numbers_method(self):
        return ''.join([x for x in self.input_str if x.isdigit()])

    def letters_method(self):
        return ''.join([x for x in self.input_str if x.isalpha()])

    def symbols_method(self):
        return ''.join([x for x in self.input_str if not x.isalnum()])

    def get_info(self):
        print(self.numbers_method())
        print(self.letters_method())
        print(self.symbols_method())


classifier = Classifier(input())
classifier.get_info()
