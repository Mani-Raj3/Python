## Input we need from the user
# Total rent
# Total foed ordered for snacking
# Electricity units spend
# Charge per unit
# Persons living in flat

# Output 
# Total amount you've to pay is..

rent = int(input("Enter your Flat rent="))
food = int(input("Enter the amount of fodd ordered ="))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit ="))
persons = int(input("Enter the number of persons living in flat ="))

# total_bill = electricity_spend * charge_per_unit

output = (food + rent  + electricity_spend * charge_per_unit) // persons

print("Each person will pay = ",output)