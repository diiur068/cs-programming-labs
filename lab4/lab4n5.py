year = int(input())

if year < 1 or year > 9999:
    print("Ошибка")
elif (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Високосный")
else:
    print("Невисокосный")
