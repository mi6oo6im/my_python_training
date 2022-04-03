capacity = float(input())
suitcases = 0
volume = 0
inline = input()
enough_room = True
while inline != "End":
    suitcases += 1
    if suitcases % 3 == 0:
        volume += float(inline) * 1.1
    else:
        volume += float(inline)
    if volume > capacity:
        suitcases -= 1
        print("No more space!")
        enough_room = False
        break
    inline = input()

if enough_room:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcases} suitcases loaded.")
