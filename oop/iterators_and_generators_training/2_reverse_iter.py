from typing import List


class reverse_iter:
    def __init__(self, items_list: List[int]):
        self.items_list = items_list
        self.i = len(self.items_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= 0:
            raise StopIteration
        self.i -= 1
        return self.items_list[self.i]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
