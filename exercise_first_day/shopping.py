# Петър иска да купи N видеокарти, M процесора и P на брой рам памет. Ако броя на видеокартите е по-голям
# от този на процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
#  Видеокарта – 250 лв./бр.
#  Процесор – 35% от цената на закупените видеокарти/бр.
#  Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.

# price variables
video_card_price = 250

# input variables

budget = float(input())
video_card_num = int(input())
processor_num = int(input())
ram_memory_num = int(input())

# calculation variables
video_card_cost = video_card_num * video_card_price

processor_price = 0.35 * video_card_cost
ram_memory_price = 0.1 * video_card_cost

processor_cost = processor_num * processor_price
ram_memory_cost = ram_memory_num * ram_memory_price

total_cost = video_card_cost + processor_cost + ram_memory_cost

if video_card_num > processor_num:
    total_cost *= 0.85

difference = abs(budget - total_cost)

if total_cost > budget:
    print(f"Not enough money! You need {difference:.2f} leva more!")
else:
    print(f"You have {difference:.2f} leva left!")
