class vowels:
    def __init__(self, text):
        self.text = text
        self.i = 0
        self.vowels = 'aeiouy'

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.text):
            raise StopIteration

        while self.text[self.i].lower() not in self.vowels:
            self.i += 1
        self.i += 1
        return self.text[self.i - 1]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
