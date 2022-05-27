capacity = 255
number_of_lines = int(input())
total_liters = 0
for line in range(number_of_lines):
    liters_of_water_to_pour = int(input())
    if liters_of_water_to_pour > capacity:
        print("Insufficient capacity!" )
        continue
    capacity -= liters_of_water_to_pour
    total_liters += liters_of_water_to_pour
print(total_liters)