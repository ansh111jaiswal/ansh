n = 4

for i in range(n):
    
    # Increasing characters
    for j in range(i + 1):
        print(chr(65 + j), end="")

    # Decreasing characters
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")

    print()