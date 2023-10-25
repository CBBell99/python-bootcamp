# Write your code below this row 👇
for number in range(1, 101):
    output = ''
    if number % 3 == 0:
        output += 'Fizz'
    if number % 5 == 0:
        output += 'Buzz'
    print(output or number)       
