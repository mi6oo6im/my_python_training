number_of_lines = int(input())
brackets = '()'
brackets_balance = 0
brackets_are_balanced = True
for _ in range(number_of_lines):
    current_string = input()
    if current_string in brackets:
        if current_string == '(':
            brackets_balance += 1
        elif current_string == ')':
            brackets_balance -= 1
        if brackets_balance > 1 or brackets_balance < 0:
            brackets_are_balanced = False
            break
if brackets_are_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
