n, m = map(int, input().split())
playground = [input().split() for _ in range(n)]

bf_pos = None
opponent_pos = []
for i in range(n):
    for j in range(m):
        if playground[i][j] == 'B':
            bf_pos = (i, j)
        elif playground[i][j] == 'P':
            opponent_pos.append((i, j))

moves = 0
touched = 0

while True:
    direction = input()
    if direction == 'Finish':
        break

    i, j = bf_pos
    if direction == 'up':
        i -= 1
    elif direction == 'down':
        i += 1
    elif direction == 'left':
        j -= 1
    elif direction == 'right':
        j += 1

    if i < 0 or i >= n or j < 0 or j >= m:
        continue

    if playground[i][j] == 'O':
        continue

    if playground[i][j] == 'P':
        touched += 1
        playground[i][j] = '-'

    bf_pos = (i, j)
    moves += 1

    if touched == 3:
        break

print('Game over!')
print(f'Touched opponents: {touched} Moves made: {moves}')
