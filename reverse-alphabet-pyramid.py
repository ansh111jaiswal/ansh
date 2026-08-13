n = 5

for i in range(n):
    
    # Spaces
    print(" " * i, end="")

    # Increasing
    for j in range(n - i):
        print(chr(65 + j), end="")

    # Decreasing
    for j in range(n - i - 2, -1, -1):
        print(chr(65 + j), end="")

    print()