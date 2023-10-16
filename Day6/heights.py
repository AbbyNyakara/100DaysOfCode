student_heights = [120, 145, 234, 125, 180, 200]

# Define the variables
total_height = 0
total_number = 0

for student in student_heights:
    total_height+=student
    total_number += 1
print(f"The average height is {round((total_height/total_number), 2)}")




