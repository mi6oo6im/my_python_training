string_list = input().split()
string_list = sorted(string_list, key=lambda x: len(x))
total_sum = 0
string_1, string_2 = string_list
sum_list = sum(
    [ord(string_1[x]) * ord(string_2[x]) if x < len(string_1) else ord(string_2[x]) for x in range(len(string_2))])
print(sum_list)
