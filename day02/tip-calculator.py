print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = input("How much would you like to tip? 10% ,12% ,15%") 
people = int(input("How many people would you like to split the bill with?"))
tip_as_a_percent = int(tip) / 100
total_tip_amount = bill * tip_as_a_percent 
total_bill = bill + total_tip_amount
split_bill = total_bill / people
formated_split_bill = "{:.2f}".format(split_bill)

print(f"Each person should pay: ${formated_split_bill}")