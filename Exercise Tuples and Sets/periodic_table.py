lines = int(input())
unique_chemicals = set()

for line in range(lines):
    input_line = input().split()
    for item in input_line:
        unique_chemicals.add(item)
for item in unique_chemicals:
    print(item)