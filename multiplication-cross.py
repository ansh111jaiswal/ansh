n = 5
mid = n // 2

for i in range(n):
    for j in range(n):

        if i == mid:
            print((i + 1) * (j + 1), end=" ")
        elif j == mid:
            print((i + 1) * (j + 1), end=" ")
        else:
            print("  ", end="")

    print()