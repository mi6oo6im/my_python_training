class sequence_repeat:
    def __init__(self, sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.index = -1
        self.sequence_len = len(sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.number - 1:
            raise StopIteration

        self.index += 1
        return self.sequence[self.index % self.sequence_len]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
