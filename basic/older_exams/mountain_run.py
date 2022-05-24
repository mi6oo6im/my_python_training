import math

record_sec = float(input())
distance_m = float(input())
seconds_per_m = float(input())

delay = math.floor(distance_m / 50) * 30

georgy_time = distance_m * seconds_per_m + delay

if georgy_time < record_sec:
    print(f"Yes! The new record is {georgy_time:.2f} seconds.")
else:
    difference = abs(georgy_time - record_sec)
    print(f"No! He was {difference:.2f} seconds slower.")
