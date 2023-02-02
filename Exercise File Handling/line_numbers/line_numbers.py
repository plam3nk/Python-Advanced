import string
from string import punctuation

with open("text.txt") as file:
    text = file.readlines()

file_output = open("output.txt", 'w')
index = 0

for line in text:
    index += 1
    marks_counter = 0
    letter_counter = 0

    for letter in line:

        if letter in string.punctuation:
            marks_counter += 1
        elif letter.isalpha():
            letter_counter += 1

    file_output.write(f"Line {index}: {''.join(line[:-1])} ({letter_counter})({marks_counter})\n")

file_output.close()

