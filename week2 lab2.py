
name=int(input("Enter your name:"))
age = int(input("Enter your age "))
course = (input("Enter your course "))
GPA = float(input("Enter your GPA "))
Local_student_status =(input("Enter your Local_Student_Status"))

current_year = 2026
birth_year = current_year - age

print("Enter your student profile")
print(f"your name is {name}")
print(f"your age is {age}")
print(f"your course is {course}")
print(f"your GPA is {GPA}")
print('YES'if Local_student_status else 'No')
