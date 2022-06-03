list_of_money = input().split(', ')
beggars = int(input())
number_beggars = []
for beggar in range(beggars):
    money_for_current_beggar = list_of_money[beggar:len(list_of_money):beggars]
    sum_for_current_beggar = sum(int(x) for x in money_for_current_beggar)
    number_beggars.append(sum_for_current_beggar)
print(number_beggars)