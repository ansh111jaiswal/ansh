n = 5
center = n // 2

for i in range(n):
    for j in range(n):
        distance = max(abs(center - i), abs(center - j))
        print(distance + 1, end="")
    print()