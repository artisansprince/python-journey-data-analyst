# control_flow.py

# This program demonstrates control flow and functions in Python

def check_age(age):
    # Function to check if the person is an adult
    if age >= 18:
        return "Adult"
    else:
        return "Not an adult"

# Input age
age = 20
print("Age:", age)
print("Status:", check_age(age))

# Loop through hobbies
for hobby in ["reading", "cycling", "hiking"]:
    print("Hobby:", hobby)

