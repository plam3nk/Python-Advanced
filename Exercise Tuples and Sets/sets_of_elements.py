number_n, number_m = input().split()
number_n = int(number_n)
number_m = int(number_m)
first_set = set()
second_set = set()
for first in range(number_n):
    number = int(input())
    first_set.add(number)
for second in range(number_m):
    number = int(input())
    second_set.add(number)
result = first_set.intersection(second_set)
for n in result:
    print(n)