start_num = input()
final_num = input()

for first_num in range(int(start_num[0]), int(final_num[0]) + 1):
    if first_num % 2 == 0:
        continue
    else:
        for second_num in range(int(start_num[1]), int(final_num[1]) + 1):
            if second_num % 2 == 0:
                continue
            else:
                for third_num in range(int(start_num[2]), int(final_num[2]) + 1):
                    if third_num % 2 == 0:
                        continue
                    else:
                        for fourth_num in range(int(start_num[3]), int(final_num[3]) + 1):
                            if fourth_num % 2 == 0:
                                continue
                            else:
                                print(f"{first_num}{second_num}{third_num}{fourth_num}", end=" ")
