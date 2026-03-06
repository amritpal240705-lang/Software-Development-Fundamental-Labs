# Student Enrolment Checker
# Author: Your Name
# Date: March 2026

# Getting student information
distance = float(input("Enter the distance from the school in km: "))
age = int(input("Enter the student's age: "))
has_right_to_stay = input("Does the student have the right to stay in New Zealand? (yes/no): ").lower()
will_pay_international_fees = input("Will the student pay international student fees? (yes/no): ").lower()

# Checking enrolment conditions
if (distance < 4 and age < 18 and has_right_to_stay == "yes") or \
   (age < 18 and will_pay_international_fees == "yes"):
    print("\nStudent can enrol at the school.")
else:
    print("\nStudent cannot enrol at the school.")