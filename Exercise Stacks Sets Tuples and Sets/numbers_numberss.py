first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
lines = int(input())

for line in range(lines):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            end = len(command)
            for index in range(2, end):
                first_set.add(int(command[index]))

        elif command[1] == "Second":
            end = len(command)
            for index in range(2, end):
                second_set.add(int(command[index]))

    elif command[0] == "Remove":
        if command[1] == "First":
            end = len(command)
            for index in range(2, end):
                if int(command[index]) in first_set:
                    first_set.remove(int(command[index]))

        elif command[1] == "Second":
            end = len(command)
            for index in range(2, end):
                if int(command[index]) in second_set:
                    second_set.remove(int(command[index]))

    elif command[0] + command[1] == "CheckSubset":
        if second_set.issubset(first_set) or first_set.issubset(second_set):
            print(True)

        else:
            print(False)

print(", ".join(str(x) for x in sorted(first_set)))
print(", ".join(str(x) for x in sorted(second_set)))

