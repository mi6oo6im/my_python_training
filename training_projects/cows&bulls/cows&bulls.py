import random

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(num_list)
random.shuffle(num_list)
print(num_list)
x = []
for _ in range(4):
    x.append(num_list.pop(0))
print(x)
print(num_list)
