
grid0= [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


print(len(grid0))

row=len(grid0)
col=len(grid0[0])

for i in range(row):
    for j in range(col):
        grid1[j][i] = grid0[i][j]


for rows in grid0:
    for clo in rows:
        print(clo,end="")
    print()


