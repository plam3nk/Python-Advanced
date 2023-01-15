from collections import deque

sequence_of_parentheses = deque(input())
open_brackets = []
while sequence_of_parentheses:
    bracket = sequence_of_parentheses.popleft()

    if bracket in "{[(":
        open_brackets.append(bracket)
    elif not open_brackets:
        print("NO")
        break
    else:
        if f"{open_brackets.pop() + bracket}" not in "{}[]()":
            print("NO")
            break
else:
    print("YES")