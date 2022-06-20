def lift_population(people: int, lift: list):
    capacity = len(lift) * 4
    all_the_people = sum(lift) + people
    for wagon in range(len(lift)):
        people_to_onboard = 4 - lift[wagon]
        if people_to_onboard > people:
            people_to_onboard = people
        lift[wagon] += people_to_onboard
        people -= people_to_onboard
        if people == 0:
            break
    if capacity > all_the_people:
        print('The lift has empty spots!')
    elif capacity < all_the_people:
        print(f"There isn't enough space! {people} people in a queue!")
    print(*lift, sep=' ')


people_in_queue = int(input())
current_lift_state = list(map(int, input().split()))
lift_population(people_in_queue, current_lift_state)
