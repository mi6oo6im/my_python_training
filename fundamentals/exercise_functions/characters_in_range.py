def characters(start_char: str, end_char: str):
    start_char_int = ord(start_char)
    end_char_int = ord(end_char)
    result_list = list(str(chr(x)) for x in range(start_char_int + 1, end_char_int) )
    return ' '.join(result_list)


start_char = input()
end_char = input()
print(characters(start_char, end_char))
