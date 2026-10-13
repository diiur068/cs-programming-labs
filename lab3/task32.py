full_name = input()

parts = full_name.split()
last_name = parts[0].capitalize()
first_name_initial = parts[1].capitalize()[0]
middle_name_initial = parts[2].capitalize()[0]

print(f"{last_name} {first_name_initial}. {middle_name_initial}.")

