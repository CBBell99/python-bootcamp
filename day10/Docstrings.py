# functions with Outputs

first = input("What's your first name?")
last = input("What's your last name?")

def format_name(f_name, l_name):
  """Take a first and last Name and format it to return a title case version  of it"""
  if f_name == '' or l_name == '':
    return "Invalid input"
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()

  return f"{formatted_f_name} {formatted_l_name}"


print(format_name(first, last)  )


#handy to get a quick explaination of code with out looking at its definition