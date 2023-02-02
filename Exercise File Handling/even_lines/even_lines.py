with open("even_lines", 'r') as even_lines:
    text = even_lines.readlines()

symbols = ["-", ",", ".", "!", "?"]
for line in range(0, len(text), 2):
    for symbol in symbols:
        while symbol in text[line]:
            text[line] = text[line].replace(symbol, '@')
    current_line = text[line].split()
    for word in range(len(current_line)-1, -1, -1):
        print(current_line[word], end=" ")
    print("")


