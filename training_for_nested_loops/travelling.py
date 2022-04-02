destination = input()
while destination != "End":
    budget = float(input())
    saved = 0
    while saved <= budget:
        saving = float(input())
        saved += saving
        if budget <= saved:
            print(f"Going to {destination}!")
            break
    destination = input()
