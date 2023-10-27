class Party:
    def __init__(self):
        self.people = []    # Instance attribute


party = Party()

name = input()
while name != "End":
    party.people.append(name)
    name = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")