# palindrome examples aba abba baab aaaaaa vaav asdfaddaasd asasaaas

def palindrome_func(text_string: str, left_index: int, right_index: int):
    palindrome_length = 1
    palindrome_text = text_string[left_index]
    while left_index >= 0 and right_index < len(text_string) and text_string[left_index] == text_string[right_index]:
        palindrome_length = right_index - left_index + 1
        palindrome_text = text_string[left_index:right_index + 1]
        left_index -= 1
        right_index += 1
    return palindrome_length, palindrome_text


text = input()
palindrome_list = []
sorted_list = []
for i in range(len(text)):
    single_center_palindrome_length, palindrome = palindrome_func(text, i, i)
    palindrome_list.append(palindrome)
    double_center_palindrome_length, palindrome = palindrome_func(text, i, i + 1)
    palindrome_list.append(palindrome)
    sorted_list = list(sorted(palindrome_list, key=lambda a: len(a), reverse=True))
print(f'The longest palindrome is {sorted_list[0]} with length {len(sorted_list[0])}')