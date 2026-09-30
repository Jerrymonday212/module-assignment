from student import student_info

name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter student course: ")

result = student_info(name, age, course)

print("\nStudent Information")
print(result)