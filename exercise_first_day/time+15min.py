# if time_seconds < 10:
#     print(f"{time_minutes:.0f}:0{time_seconds:.0f}")
# else:
#     print(f"{time_minutes:.0f}:{time_seconds:.0f}")

# Резултатът да се отпечата във формат часове:минути. Часовете
# винаги са между 0 и 23, а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.

time_now_hh = int(input())
time_now_mm = int(input())

time_now_minutes = (time_now_hh * 60) + time_now_mm

time_now_minutes_plus_15 = time_now_minutes + 15

time_now_hh_plus_15 = time_now_minutes_plus_15 // 60
time_now_mm_plus_15 = time_now_minutes_plus_15 % 60

if time_now_hh_plus_15 > 23:
    print(f'{time_now_hh_plus_15 - 24}:{time_now_mm_plus_15:02d}')
else:
    print(f'{time_now_hh_plus_15}:{time_now_mm_plus_15:02d}')
