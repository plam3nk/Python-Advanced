import os

input_line = input()

while input_line != "End":

    input_line = input_line.split("-")
    action = input_line[0]
    file_name = input_line[1]

    if action == "Create":
        file = open(f"{file_name}", 'w')
        file.close()
    elif action == "Add":

        content = input_line[2]
        if file_name:
            with open(f"{file_name}", 'a') as file:
                file.write(f"{content}\n")

    elif action == "Replace":
        try:
            new_string = input_line[3]
            old_string = input_line[2]

            with open(f"{file_name}", 'r+') as file:
                lines = file.readlines()

                for index in range(len(lines)):
                    lines[index] = lines[index].replace(old_string, new_string)
                file.write("".join(lines))

        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        try:
            os.remove(f"{file_name}")
        except FileNotFoundError:
            print("An error occurred")

    input_line = input()
