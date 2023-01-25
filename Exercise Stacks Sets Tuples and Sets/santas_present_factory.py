from collections import deque


def crafter(number):
    if number == 150:
        return "Doll"
    elif number == 250:
        return "Wooden train"
    elif number == 300:
        return "Teddy bear"
    elif number == 400:
        return "Bicycle"


materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

crafted_items = {}
crafted = False
while materials and magic_levels:
    current_materials = materials.pop()
    current_magic = magic_levels.popleft()

    if current_magic == 0 and current_materials == 0:
        continue
    if current_magic == 0:
        materials.append(current_materials)
        continue
    if current_materials == 0:
        magic_levels.insert(0, current_magic)
        continue

    multiplication = current_materials * current_magic
    if multiplication < 0:
        materials.append((current_materials + current_magic))
    elif multiplication > 0:
        if multiplication in [150, 250, 300, 400]:
            item = crafter(multiplication)
            if item not in crafted_items:
                crafted_items[item] = 1
            else:
                crafted_items[item] += 1

        else:
            materials.append(current_materials)
            materials[-1] += 15
    if "Doll" in crafted_items and "Wooden train" in crafted_items:
        crafted = True

    elif "Teddy bear" in crafted_items and "Bicycle" in crafted_items:
        crafted = True

if crafted:
    print("The presents are crafted! Merry Christmas!")

if not crafted:
    print("No presents this Christmas!")

if materials:
    print("Materials left:", end=" ")
    print(", ".join(str(x) for x in materials[::-1]))
if magic_levels:
    print(f"Magic left:", end=" ")
    print(", ".join(str(x) for x in magic_levels))
for toy in sorted(crafted_items.keys()):
    print(f"{toy}: {crafted_items[toy]}")
