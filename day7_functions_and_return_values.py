# Day 7: Functions and Return Values in Python

# 🌟 Example 1: Basic function definition
def greet():
    print("Hello Bhagya! Welcome to Day 7 of your DSA journey 🚀")

# Calling the function
greet()

print("----------------------------")

# 🌟 Example 2: Function with parameters
def add_numbers(a, b):
    print(f"The sum of {a} and {b} is:", a + b)

# Calling the function with different arguments
add_numbers(5, 7)
add_numbers(10, 15)

print("----------------------------")

# 🌟 Example 3: Function with return value
def multiply(a, b):
    result = a * b
    return result

product = multiply(4, 5)
print("Product of 4 and 5 is:", product)

print("----------------------------")

# 🌟 Example 4: Function returning multiple values
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division

a, s, m, d = calculate(8, 2)
print("Addition:", a)
print("Subtraction:", s)
print("Multiplication:", m)
print("Division:", d)

print("----------------------------")

# 🌟 Example 5: Default and keyword arguments
def greet_user(name="User", msg="Good Morning!"):
    print(f"Hello {name}, {msg}")

greet_user()
greet_user("Bhagya")
greet_user(msg="Good Evening!", name="Bhagya")

print("----------------------------")

# 🌟 Example 6: Function with variable number of arguments (*args)
def print_numbers(*nums):
    print("Numbers passed:", nums)
    total = sum(nums)
    print("Sum of numbers:", total)

print_numbers(1, 2, 3, 4)
print_numbers(10, 20)

print("----------------------------")

# 🌟 Example 7: Function with keyword arguments (**kwargs)
def show_details(**info):
    print("User Details:")
    for key, value in info.items():
        print(f"{key} : {value}")

show_details(name="Bhagya", age=19, course="BTech AIML", goal="Master DSA with Python")

print("----------------------------")

# 🌟 Example 8: Function calling another function
def square(num):
    return num * num

def display_square(n):
    print(f"The square of {n} is {square(n)}")

display_square(6)

print("----------------------------")

# 🌟 Example 9: Recursive Function (Factorial Example)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"Factorial of {num} is {factorial(num)}")

print("----------------------------")

print("✅ All function examples executed successfully!")
