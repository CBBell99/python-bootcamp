# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size.lower() == 's':
    bill += 15
elif size.lower() == 'm':
    bill += 20   
elif size.lower() == 'l':
    bill += 25

if add_pepperoni.lower() == 'y':
    if size.lower() == 's':
        bill += 2
    else: 
        bill += 3

if extra_cheese.lower() == 'y': 
    bill += 1
    
print(f"Your final bill is: ${bill}.")   
