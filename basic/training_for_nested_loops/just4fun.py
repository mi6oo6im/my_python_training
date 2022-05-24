text = input()
txt = []
for i in range(len(text)):
    print(text[i])
    txt.append(text[i])
    print(txt)

for i in txt:
    txt.pop()
    print(txt)
