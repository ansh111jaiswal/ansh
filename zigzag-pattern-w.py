rows = 4
cols = 12

for i in range(rows):
    for j in range(cols):
        if (i + j) % 4 == 0 or (i == 1 and j % 4 == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()