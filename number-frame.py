n = 6

for i in range(n):
    for j in range(n):
        if j <= i:
            print(i - j + 1, end="")
        else:
            print(j - i + 1, end="")
    print()