n = 4

for i in range(n, 0, -1):
    start = i * (i - 1) // 2 + 1

    for j in range(i):
        print(start + j, end=" ")

    print()