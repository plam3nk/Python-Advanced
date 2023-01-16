lines = int(input())

row = 0
odd_set = set()
even_set = set()

for line in range(lines):
    row += 1
    name = input()
    name_sum = sum([int(ord(x)) for x in name]) // row
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    elif name_sum % 2 != 0:
        odd_set.add(name_sum)

odd_set_sum = sum(x for x in odd_set)
even_set_sum = sum(x for x in even_set)
result = 0

if odd_set_sum == even_set_sum:
    result = even_set.union(odd_set)

elif odd_set_sum > even_set_sum:
    result = odd_set.difference(even_set)

elif even_set_sum > odd_set_sum:
    result = even_set.symmetric_difference(odd_set)

result = [str(x) for x in result]
print(", ".join(result))
