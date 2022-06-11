def is_palindrome(list_of_numbers: list):
    result = []
    for i in list_of_numbers:
        if i == i[-1::-1]:
            result += ['True']
        else:
            result += ['False']
    return result


list_of_numbers = input().split(', ')
print(*is_palindrome(list_of_numbers), sep='\n')
