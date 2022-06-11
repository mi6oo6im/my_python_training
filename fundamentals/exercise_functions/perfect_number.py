def perfect_number_check(number: str):
    positive_divisors = []
    for num in range(1, int(number)):
        if int(number) % int(num) == 0:
            positive_divisors.append(int(num))
    if sum(positive_divisors) == int(number):
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


number = input()
perfect_number_check(number)
