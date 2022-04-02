first_num_limit = int(input())
second_num_limit = int(input())
third_num_limit = int(input())

for num1 in range(1, first_num_limit + 1):
    if num1 % 2 != 0:
        continue
    else:
        for num2 in range(2, second_num_limit + 1):
            is_prime = True
            for denominator in range(2, num2):
                if num2 % denominator == 0:
                    is_prime = False
                    continue
            if not is_prime:
                continue
            else:
                for num3 in range(1, third_num_limit + 1):
                    if num3 % 2 != 0:
                        continue
                    else:
                        print(f"{num1} {num2} {num3}")
