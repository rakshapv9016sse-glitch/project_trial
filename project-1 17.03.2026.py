student={}
def add_student(name,marks):
    student[name]=marks
    print("student added")
def display_student():
    for name,marks in student.items():
        print(name,":",marks)
add_student("raksha",90)
add_student("divakar",95)
display_student()