dictionary = {
    88: "Hello",
    86: "How are you?",
}
message_count = int(input())
code = ''
message = ''

for _ in range(message_count):
    code = int(input())
    if code not in dictionary:
        if code < 88:
            message = "GREAT!"
        else:
            message = "Bye."
    else:
        message = dictionary[code]
    print(message)
