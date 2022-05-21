# lists are like javascript arrays
# lists can contain multiple types of data
# lists are zero indexed

states_of_america = ["Delaware", "Pennsylvania", "Texas"]

print(states_of_america[0])

# save Texas to a variable
state = states_of_america[2]

# reassign list item
states_of_america[1] = "Pencilvania"

# add item to list.  Works like .push()
states_of_america.append("Belltron")

# concatenate list
states_of_america.extend(["hey", "yall"])

print(len(states_of_america))
print(states_of_america)

# Will get error as index doesn"t exist
print(states_of_america[7])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries",  "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale",  "Tomatoes", "Celery", "Potatoes"]

# Nested list
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
