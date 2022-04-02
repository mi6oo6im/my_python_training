array = [200, 100, 50, 20, 10, 5, 2, 1]
change = float(input())
stotinki = int(change * 100)
coins = 0
for coin in array:
    coins += stotinki // coin
    stotinki = stotinki % coin
print(coins)
