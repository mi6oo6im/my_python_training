command = input()
prime_sum = 0
non_prime_sum = 0

while command != "stop":
    number = int(command)
    is_prime = True
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    for num in range(2, number):
        if number == 0 or number % num == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        prime_sum += number
    else:
        non_prime_sum += number
    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
