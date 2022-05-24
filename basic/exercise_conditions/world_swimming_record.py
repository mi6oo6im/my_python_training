# На конзолата се въвежда
# рекордът в секунди, който Иван трябва да подобри, разстоянието в метри, което трябва да преплува и
# времето в секунди, за което плува разстояние от 1 м. Да се напише програма, която изчислява дали се е
# справил със задачата, като се има предвид, че: съпротивлението на водата го забавя на всеки 15 м. с 12.5
# секунди. Когато се изчислява колко пъти Иванчо ще се забави, в резултат на съпротивлението на водата,
# резултатът трябва да се закръгли надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иванчо ще преплува разстоянието и разликата спрямо
# Световния рекорд.

# input variables
old_record_in_sec = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())

# calculation variables
delay_in_sec = (distance_in_meters // 15) * 12.5

total_time = distance_in_meters * time_per_meter + delay_in_sec

if total_time < old_record_in_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    seconds_more = total_time - old_record_in_sec
    print(f"No, he failed! He was {seconds_more:.2f} seconds slower.")
