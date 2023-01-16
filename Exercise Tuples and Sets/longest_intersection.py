lines = int(input())
longest_intersection = set()

for line in range(lines):
    first_range, second_range = input().split("-")
    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")

    first_set = set(x for x in range(int(first_start), int(first_end) + 1))

    second_set = set(x for x in range(int(second_start), int(second_end) + 1))

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

longest_intersection = tuple(str(x) for x in longest_intersection)

print("Longest intersection is [", end="")
print(", ".join(longest_intersection), end="")
print(f"] with length {len(longest_intersection)}")