# Day 4: Conditional Statements in Python

# 🌟 Example 1: Basic if statement
age = 18
if age >= 18:
    print("You are eligible to vote!")

print("----------------------------")

# 🌟 Example 2: if-else statement
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an Even number")
else:
    print(f"{num} is an Odd number")

print("----------------------------")

# 🌟 Example 3: if-elif-else ladder
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 45:
    print("Grade: C")
else:
    print("Grade: F")

print("----------------------------")

# 🌟 Example 4: Nested if statements
num = int(input("Enter another number: "))
if num >= 0:
    if num == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")

print("----------------------------")

# 🌟 Example 5: Short Hand if and if-else
a = 10
b = 5

# One line if
if a > b: print("a is greater than b")

# One line if-else
print("a is greater") if a > b else print("b is greater")

print("----------------------------")

# 🌟 Example 6: Checking multiple conditions together
username = "Bhagya"
password = "Python123"

if username == "Bhagya" and password == "Python123":
    print("Login Successful ✅")
else:
    print("Invalid Username or Password ❌")