# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("hello")
#   print("world")
#   print("!")

# greet()

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print("How do you do?")
#   print("Isn't the weather nice today?")

# greet_with_name("Chris")  

def greet_with(name, location):
  print(f"Hi {name}")
  print(f"Are you from {location}?")

# greet_with("chris", "vancouver")
# keyword aruguments
greet_with(location="Vancover", name="Chris")