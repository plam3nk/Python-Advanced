from modules import create_sequence, locate

command = input()
while command != "Stop":
    command = command.split()
    if command[0] == "Create":
        sequence = create_sequence(int(command[2]))
        print(*sequence)
    elif command[0] == "Locate":
        try:
            index = locate(command[1], *sequence)
            if index:
                print(f"The number - {command[1]} is at index {index}")
            else:
                print(f"The number {command[1]} is not in the sequence")
        except NameError:
            print("Create sequence first!")

    command = input()
