from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

my_meds = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

while textiles and medicaments:
    result = textiles[0] + medicaments[-1]

    if result == 30:
        my_meds["Patch"] += 1
        textiles.popleft()
        medicaments.pop()

    elif result == 40:
        my_meds["Bandage"] += 1
        textiles.popleft()
        medicaments.pop()

    elif result == 100:
        my_meds["MedKit"] += 1
        textiles.popleft()
        medicaments.pop()

    else:
        if result > 100:
            my_meds["MedKit"] += 1
            textiles.popleft()
            medicaments.pop()
            diff = result - 100
            medicaments[-1] += diff

        else:
            textiles.popleft()
            medicaments[-1] += 10


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_dict = sorted(
    my_meds.items(),
    key=lambda x: (-x[1], x[0])
)

for item, quantity in sorted_dict:
    if quantity != 0:
        print(f"{item} - {quantity}")

if medicaments:
    print(f"Medicaments left: ", end='')
    for el in range(len(medicaments) - 1, -1, -1):
        if el == 0:
            print(medicaments[el], end='')
        else:
            print(medicaments[el], end=', ')

elif textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")