# Write a function get_student_grade(student_grades, name) that takes a 
# dictionary student_grades where keys are student names and values are grades,
# and returns the grade of the student name. If the student is not in the 
# dictionary, it prints "Error: student not found"

def get_student_grade(student_grades, name):
    try:
        return student_grades[name]
    except LookupError:
        raise ValueError("student not found")

unipi = {"Imane Rajy": 33, "Luca Seggiani": 29, "Pippo Stocazzi": 18}
while True:
    try:
        print(get_student_grade(unipi, input("Enter student name: ")))
    except ValueError:
        print("No such student")
