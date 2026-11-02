count = 0
total_sum = 0

while True:
    user_input = input()
    if user_input == "stop":
        break

    price = int(user_input)
    total_sum += price
    count += 1

if count == 0:
    print("Нет покупок")
else:
    average = total_sum / count
    print(f"Покупок: {count}")
    print(f"Общая стоимость: {total_sum} руб")
    print(f"Средняя стоимость: {average:.2f} руб")
