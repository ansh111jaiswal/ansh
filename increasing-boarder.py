rows = 4
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1:
            print(j + 1, end="")
        elif j == 0:
            print("1", end="")
        elif j <= i:
            print(j + 1, end="")
        elif j == cols - 1:
            print(cols, end="")
        else:
            print(" ", end="")
    print()