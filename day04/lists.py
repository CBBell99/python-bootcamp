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

print(states_of_america)
