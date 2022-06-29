class Party:
    def __init__(self):
        self.people = []

    def going(self):
        people_going = ', '.join(self.people)
        return f'Going: {people_going}\nTotal: {len(self.people)}'


command = input()
party = Party()

while command != 'End':
    party.people.append(command)
    command = input()

print(party.going())
