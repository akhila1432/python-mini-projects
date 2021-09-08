user_input = input("hey enter the number of days to you want to calculate?\n")
user_input_number = int(user_input)
calculation_to_units = 24
name_of_units = "hours"
def days_to_units(number_of_days):
 return f"{number_of_days} days {number_of_days *calculation_to_units} {name_of_units}"
calculated_value = days_to_units(user_input_number)
print(calculated_value)
