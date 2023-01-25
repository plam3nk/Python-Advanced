from collections import deque

substrings = deque(input().split())
colors = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

collected_colors = []

while substrings:
    first = substrings.popleft()
    second = substrings.pop() if substrings else ''

    for color in (first + second, second + first):
        if color in colors:
            collected_colors.append(color)
            break
    else:
        for item in (first[:-1], second[:-1]):
            if item:
                substrings.insert(len(substrings) // 2, item)

for color in set(secondary_colors.keys()).intersection(collected_colors):
    if not secondary_colors[color].issubset(collected_colors):
        collected_colors.remove(color)

print(collected_colors)