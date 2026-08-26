n = 5

for i in range(n):
    for j in range(n):

        if i == 0:
            print(j + 1, end="")
        elif i == n - 1:
            print(n - j, end="")
        elif j == 0:
            print(i + 1, end="")
        elif j == n - 1:
            print(n - i, end="")
        else:
            print(" ", end="")

    print()