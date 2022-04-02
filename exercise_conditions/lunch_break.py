# По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да
# напишете програма, с която ще разберете дали имате достатъчно време да изгледате епизода. По време на
# почивката отделяте време за обяд и време за отдих. Времето за обяд ще бъде 1/8 от времето за почивка, а
# времето за отдих ще бъде 1/4 от времето за почивка.
import math

# input variables

show_name = input()
episode_length = int(input())
break_length = int(input())

# calculation variables

lunch_time = 0.125 * break_length
relax_time = 0.25 * break_length

needed_time = episode_length + lunch_time + relax_time

difference = math.ceil(abs(needed_time - break_length))

if needed_time > break_length:
    print(f"You don't have enough time to watch {show_name}, you need {difference:.0f} more minutes.")
else:
    print(f"You have enough time to watch {show_name} and left with {difference:.0f} minutes free time.")
