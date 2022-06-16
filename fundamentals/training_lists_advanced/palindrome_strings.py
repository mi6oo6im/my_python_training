def is_palindrome(text_string: str):
    reversed_text = text_string[::-1]
    if text_string == reversed_text:
        return True
    else:
        return False


text_list = input().split()
palindrome = input()
palindrome_list = list(filter(is_palindrome, text_list))
print(palindrome_list)
palindrome_count = palindrome_list.count(palindrome)
print(f'Found palindrome {palindrome_count} times')