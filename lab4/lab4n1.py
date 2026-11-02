current_temp = float(input())
desired_temp = float(input())

if current_temp > desired_temp:
    print("Охлаждение")
elif current_temp < desired_temp:
    print("Нагрев")
else:
    print("Выключен")
