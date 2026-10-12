phone = input()

cleaned_phone = phone.replace("+", "")
cleaned_phone = cleaned_phone.replace(" ", "")
cleaned_phone = cleaned_phone.replace("(", "")
cleaned_phone = cleaned_phone.replace(")", "")
cleaned_phone = cleaned_phone.replace("-", "")

print(cleaned_phone)
