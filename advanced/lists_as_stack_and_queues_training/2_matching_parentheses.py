expression = input()
parentheses = []
for i in range(len(expression)):
    if expression[i] == '(':
        parentheses.append(i)
    elif expression[i] == ')':
        last = parentheses.pop()
        print(expression[last: i + 1])
