train_data = input()

info = train_data.split(";")

train_number = info[0]
departure_city = info[1]
arrival_city = info[2]
time = info[3]
price = float(info[4])

print("Поезд:", train_number)
#print("Маршрут:", departure_city, "-", arrival_city)
print(f"Маршрут: {departure_city} - {arrival_city}")
print("Отправление:", time)
print(f"Цена: {price:.2f} руб")
