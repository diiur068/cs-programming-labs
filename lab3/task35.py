identifier = input()

length = len(identifier)

only_letters = identifier.isalpha()
only_digits = identifier.isdigit()
alphanumeric = identifier.isalnum()

has_hyphen = "-" in identifier

print("Длина:", length)
print("Только буквы:", only_letters)
print("Только цифры:", only_digits)
print("Буквенно-цифровая:", alphanumeric)
print("Содержит дефис:", has_hyphen)
