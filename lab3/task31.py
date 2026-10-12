doc_code = input()

category = doc_code[0:3]
year = doc_code[4:8]
number = doc_code[9:13]
reversed_number = number[::-1]

print("Категория:", category)
print("Год:", year)
print("Номер:", number)
print("Обратный номер:", reversed_number)
