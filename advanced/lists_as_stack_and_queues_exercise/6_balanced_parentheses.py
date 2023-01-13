from collections import deque

opening_brackets = ['(', '[', '{']
closing_brackets = [')', ']', '}']
sequence = deque(list(input()))
stack = []
is_balanced = True
while sequence:
    current = sequence.popleft()
    if current in opening_brackets:
        stack.append(current)
    else:
        if stack and stack[-1] == opening_brackets[closing_brackets.index(current)]:
            stack.pop()
        else:
            is_balanced = False
            break

if is_balanced:
    print('YES')
else:
    print('NO')
