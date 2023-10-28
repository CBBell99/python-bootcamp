# dictionaries in Python are a collection of key/value pairs not unlike a JS object or hash table if you're fancy
# trailing commas are ok
# like JSON.  strings must be in quotes

programming_dictionary ={
  "Bug": "An error in a programn that prevents the progream from running as expected",
  "Function": "A piece of code that you can easily call over and over again",
}

# prints all entries in dict
print(programming_dictionary)

# prints value of key in dict
print(programming_dictionary['Bug'])

# can add entries like so
programming_dictionary['Loop'] =  "The action of doing something over and over again"

print(programming_dictionary)

# can also instantiate a new dict like so
empty_dictionary = {}
my_dict = dict()

# can redefine like so
# programming_dictionary["Bug"] = 'poop'

# Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])