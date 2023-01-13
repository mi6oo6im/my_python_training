def is_balanced(expr):
    stack = []
    for char in expr:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return "NO"
            if char == ")" and stack[-1] != "(":
                return "NO"
            if char == "]" and stack[-1] != "[":
                return "NO"
            if char == "}" and stack[-1] != "{":
                return "NO"
            stack.pop()
    if not stack:
        return "YES"
    else:
        return "NO"


print(is_balanced(input()))
