def reverse_text(text):
    for x in reversed(text):
        yield x


for char in reverse_text("step"):
    print(char, end='')

