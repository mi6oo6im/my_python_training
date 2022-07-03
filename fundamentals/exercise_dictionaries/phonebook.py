input_line = input()
phonebook_dict = {}
while '-' in input_line:
    name, number = input_line.split('-')
    phonebook_dict[name] = number
    input_line = input()
contact_queries = int(input_line)
for _ in range(contact_queries):
    contact_name = input()
    if contact_name in phonebook_dict:
        print(f'{contact_name} -> {phonebook_dict[contact_name]}')
    else:
        print(f"Contact {contact_name} does not exist.")
