def tribunacci_row(number: int):
    tribunacci_list = [1]
    for i in range(1, number):
        start_index = i - 3
        end_index = i
        if start_index < 0:
            start_index = 0
        tribunacci_list.append(sum(tribunacci_list[start_index:end_index]))
    tribunacci_string_list = [str(x) for x in tribunacci_list]
    return ' '.join(tribunacci_string_list)


number_of_figures = int(input())
print(tribunacci_row(number_of_figures))
