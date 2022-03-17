hour_exam = int(input())
minute_exam = int(input())
hour_come = int(input())
minute_come = int(input())

minutes_only_exam = hour_exam * 60 + minute_exam
minutes_only_come = hour_come * 60 + minute_come

difference = abs(minutes_only_come - minutes_only_exam)

diff_hour = difference // 60
diff_minute = difference % 60

if minutes_only_exam < minutes_only_come:
    print("Late")
elif minutes_only_exam - 30 <= minutes_only_come <= minutes_only_exam:
    print("On time")
else:
    print("Early")

if minutes_only_exam - 60 < minutes_only_come < minutes_only_exam:
    print(f"{difference} minutes before the start")
elif minutes_only_exam - 60 >= minutes_only_come:
    print(f"{diff_hour}:{diff_minute:02d} hours before the start")
elif minutes_only_exam + 60 > minutes_only_come > minutes_only_exam:
    print(f"{difference} minutes after the start")
elif minutes_only_exam + 60 <= minutes_only_come:
    print(f"{diff_hour}:{diff_minute:02d} hours after the start")
