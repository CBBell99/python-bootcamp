# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_heights = 0
number_of_students = len(student_heights)

for height in student_heights:
    total_heights += height

average_height = total_heights/number_of_students
rounded_total = round(average_height)
print(f"total height = {total_heights}")
print(f"number of students = {number_of_students}")
print(f"average height = {rounded_total}")

