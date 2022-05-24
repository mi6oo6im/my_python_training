command = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0


while command != "Finish":
    movie_name = command
    capacity = int(input())
    count_tickets = 0
    while count_tickets < capacity:
        ticket_type = input()
        if ticket_type == "End":
            break
        count_tickets += 1
        total_tickets += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        else:
            kids_tickets += 1
    capacity_percent = count_tickets / capacity * 100
    print(f"{movie_name} - {capacity_percent:.2f}% full.")
    command = input()

student_tickets_percent = student_tickets / total_tickets * 100
standard_tickets_percent = standard_tickets / total_tickets * 100
kids_tickets_percent = kids_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_percent:.2f}% student tickets.")
print(f"{standard_tickets_percent:.2f}% standard tickets.")
print(f"{kids_tickets_percent:.2f}% kids tickets.")
