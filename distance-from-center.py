n = 5
center = n // 2

for i in range(n):
    for j in range(n):
        value = abs(center - i) + abs(center - j)
        print(value, end=" ")
    print()