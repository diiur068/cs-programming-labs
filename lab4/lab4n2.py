base_price = float(input())
age = int(input())

if base_price <= 0 or age < 0 or age > 120:
    print("Ошибка")
elif 0 <= age <= 5:
    final_price = base_price * 0.0
    print(f"Стоимость: {final_price:.2f} руб")
elif 6 <= age <= 17:
    final_price = base_price * 0.5
    print(f"Стоимость: {final_price:.2f} руб")
elif 18 <= age <= 59:
    final_price = base_price * 1.0
    print(f"Стоимость: {final_price:.2f} руб")
else:
    final_price = base_price * 0.7
    print(f"Стоимость: {final_price:.2f} руб")
