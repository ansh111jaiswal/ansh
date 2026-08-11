n = 7

for i in range(n):
    if i <= n // 2:
        spaces = i
        width = n - 2 * i
    else:
        spaces = n - i - 1
        width = 2 * (i - n // 2) + 1

    print(" " * spaces, end="")

    if width == 1:
        print("*")
    else:
        print("*" + " " * (width - 2) + "*")