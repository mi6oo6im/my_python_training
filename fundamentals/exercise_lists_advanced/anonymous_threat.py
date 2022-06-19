def merge_string(string_list: list):
    return [''.join(string_list)]


def divide_string(string: str, partition_count: int):
    partition_length = len(string) // partition_count
    last_partition = partition_length + len(string) % partition_count
    partitioned_string = [string[partition_length * x: partition_length * x + partition_length]
                          for x in range(partition_count - 1)]
    partitioned_string.append(string[-last_partition::])
    return partitioned_string


data_array = input().split()
command = input()
while command != '3:1':
    type_command, first_param, second_param = command.split()
    new_data_array = []
    if type_command == 'merge':
        start_index = int(first_param)
        if start_index < 0:
            start_index = 0
        end_index = int(second_param)
        if end_index >= len(data_array):
            end_index = len(data_array) - 1
        merged_string = merge_string(data_array[start_index:end_index + 1])
        new_data_array = data_array[0:start_index] + merged_string + data_array[end_index + 1::]
    elif type_command == 'divide':
        index = int(first_param)
        partitions = int(second_param)
        divided_string_list = divide_string(data_array[index], partitions)
        data_array.pop(index)
        for i in range(len(divided_string_list)-1, -1, -1):
            data_array.insert(index, divided_string_list[i])
        new_data_array = data_array
    data_array = new_data_array
    command = input()
print(*data_array, sep=' ')
