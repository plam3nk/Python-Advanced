from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]


items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100,
}

created_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_med = medicaments.pop()

    sum_of_both = current_textile + current_med

    if sum_of_both == 30 or sum_of_both == 40 or sum_of_both == 100:
        for k, v in items.items():
            if sum_of_both == v:
                created_items[k] += 1

    elif sum_of_both > 100:
        created_items["MedKit"] += 1
        diff = sum_of_both - 100
        medicaments[-1] += diff

    else:
        current_med += 10
        medicaments.append(current_med)

if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")


if created_items:
    sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_items:
        if value != 0:
            print(f'{key} - {value}')

if medicaments:
    reversed_meds = []
    for i in range(len(medicaments) -1, -1, -1):
        reversed_meds.append(medicaments[i])
    print("Medicaments left: ", end="")
    print(*reversed_meds, sep=", ")

if textiles:
    print("Textiles left: ", end="")
    print(*textiles, sep=", ")