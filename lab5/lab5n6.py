n = int(input())
odd_count = 0

for r in range(n):
    c = 1
    for k in range(r + 1):
        if c % 2 != 0:
            odd_count += 1

        if k < r:
            print(c, end=" ")
            c = c * (r - k) // (k + 1)
        else:
            print(c)

print(f"Нечетных элементов: {odd_count}")
