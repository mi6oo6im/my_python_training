folder_path = 'files/'
words_file = folder_path + 'words.txt'
input_file = folder_path + 'input.txt'
output_file = folder_path + 'output.txt'
words_dict = {}
with open(words_file, 'r') as file:
    file2 = open(input_file)
    data = file2.read()
    for line in file:
        for word in line.split():
            words_dict[word] = data.count(word)
    file2.close()
sorted_list = sorted(words_dict.items(), key=lambda x: -x[1])
result = '\n'.join(f'{k} - {v}' for k, v in sorted_list)

with open(output_file, 'w') as file:
    file.write(result)
