clothes = [int(x) for x in input().split()]
capacity_of_rack = int(input())
racks = 0
current_rack_space = 0
while clothes:
    clothe = clothes.pop()
    if current_rack_space - clothe >= 0:
        current_rack_space -= clothe
    else:
        racks += 1
        current_rack_space = capacity_of_rack - clothe

print(racks)