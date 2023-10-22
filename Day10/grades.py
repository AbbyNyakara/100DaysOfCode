'''
 A programe to classify student grades
'''

grades = {
    "Henry": 55,
    "Abby": 79,
    "Carl": 97,
    "Matthew": 88,
    "Eli": 77,
    "Neville": 68
}

#Given the following info: 
#{91-100: "Outstanding", 81-90: "Exceeds expectation, 71-80: "Acceptable", 70/lower: "Fail"}
# Classify each student


student_grades = {}

for student, grade in grades.items():
    if grade >= 91:
        grade = "Outstanding"
    elif grade >= 81:
        grade = "Exceeds Expectation"
    elif grade >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[student] = grade

print(student_grades)
    
    