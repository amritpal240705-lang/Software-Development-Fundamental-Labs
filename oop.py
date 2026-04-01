# Student Attendance Tracking System

students = []          # this list will store all students
student_id = 1000      # starting student ID


# function to add student
def add_student():
    global student_id   # use global ID

    # take input from user
    name = input("Enter student name: ")
    course = input("Enter course name: ")
    attendance = float(input("Enter attendance %: "))

    # increase student ID
    student_id = student_id + 1

    # add student data into list
    students.append([student_id, name, course, attendance])

    # print message
    print("Student added")
    print("ID is:", student_id)


# function to update student
def update_student():
    id = int(input("Enter student ID: "))

    # check each student in list
    for s in students:
        if s[0] == id:   # check ID match
            print("Student found")

            # update course and attendance
            s[2] = input("Enter new course: ")
            s[3] = float(input("Enter new attendance: "))

            print("Updated")
            return   # stop here

    # if ID not found
    print("Student not found")


# function to show all students
def show_students():
    if len(students) == 0:
        print("No data")
    else:
        # print all students
        for s in students:
            print("ID:", s[0])
            print("Name:", s[1])
            print("Course:", s[2])
            print("Attendance:", s[3], "%")
            print("-----")


# function to find average attendance
def average_attendance():
    if len(students) == 0:
        print("No data")
        return

    total = 0

    # add all attendance values
    for s in students:
        total = total + s[3]

    # calculate average
    avg = total / len(students)

    print("Average attendance:", avg)


# menu (runs again and again)
while True:
    print("\n1. Add")
    print("2. Update")
    print("3. Show")
    print("4. Average")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        show_students()
    elif choice == "4":
        average_attendance()
    elif choice == "5":
        print("End")
        break
    else:
        print("Wrong choice")