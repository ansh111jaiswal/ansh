n = 5

for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print(i + 1, end=" ")
        else:
            print(" ", end=" ")
    print()