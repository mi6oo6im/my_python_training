a = input()
b = ""
movie = ""
seat_type = ""
total_seats = 0
this_movie_tickets = 0
total_tickets = 0
capacity_taken = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
student_percent = 0
standard_percent = 0
kid_percent = 0

while True:
    movie = a
    total_seats = int(input())
    this_movie_tickets = 0
    capacity_taken = 0
    b = input()
    if b == "Finish":
        break
    while b != "End":
        seat_type = b
        this_movie_tickets += 1
        total_tickets += 1
        if seat_type == "student":
            student_tickets += 1
        elif seat_type == "kid":
            kid_tickets += 1
        elif seat_type == "standard":
            standard_tickets += 1
        b = input()
        if b == "Finish":
            break
    capacity_taken = this_movie_tickets / total_seats * 100
    print(f"{movie} - {capacity_taken:.2f}% full.")
    if b == "Finish":
        break
    a = input()


student_percent = student_tickets / total_tickets * 100
kid_percent = kid_tickets / total_tickets * 100
standard_percent = standard_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")
