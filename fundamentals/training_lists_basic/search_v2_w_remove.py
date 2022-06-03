number_of_lines = int(input())
filter_str = input()
list_of_all_texts = []
for _ in range(number_of_lines):
    current_text = input()
    list_of_all_texts.append(current_text)
print(list_of_all_texts)

for text in range(len(list_of_all_texts)-1, -1, -1):
    element = list_of_all_texts[text]
    if filter_str not in element:
        list_of_all_texts.remove(element)
print(list_of_all_texts)
