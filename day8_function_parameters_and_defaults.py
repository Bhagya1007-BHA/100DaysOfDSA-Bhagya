# Day 8: Function Parameters and Default Arguments in Python

# 🌟 Example 1: Positional Arguments
def student_details(name, age, course):
    print(f"Name: {name}, Age: {age}, Course: {course}")

# The order of arguments matters
student_details("Bhagya", 19, "AIML")

print("----------------------------")

# 🌟 Example 2: Keyword Arguments
student_details(course="AIML", name="Adithya", age=20)

print("----------------------------")

# 🌟 Example 3: Default Arguments
def greet_user(name, message="Welcome to DSA Practice!"):
    print(f"Hello {name}, {message}")

# message has a default value
greet_user("Bhagya")
greet_user("Bhanu", "Keep up your GitHub streak! 🔥")

print("----------------------------")

# 🌟 Example 4: Mixing Positional and Keyword Arguments
def order(item, quantity, price):
    print(f"Item: {item}, Quantity: {quantity}, Total Price: ₹{quantity * price}")

order("Notebook", 3, 50)
order(item="Pen", quantity=5, price=10)
order("Bag", quantity=1, price=400)

print("----------------------------")

# 🌟 Example 5: Variable-Length Arguments (*args)
def sum_all(*numbers):
    print("Numbers:", numbers)
    total = sum(numbers)
    print("Sum of all numbers:", total)

sum_all(1, 2, 3)
sum_all(10, 20, 30, 40, 50)

print("----------------------------")

# 🌟 Example 6: Variable-Length Keyword Arguments (**kwargs)
def user_profile(**details):
    print("User Profile Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

user_profile(name="Bhagya", course="BTech AIML", year="3rd", goal="GATE 2026 Topper")

print("----------------------------")

# 🌟 Example 7: Combining *args and **kwargs
def display_info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

display_info(1, 2, 3, name="Bhagya", subject="Python", progress="8 Days Streak 💫")

print("----------------------------")

# 🌟 Example 8: Using Functions with Return Values
def average_marks(*marks):
    total = sum(marks)
    avg = total / len(marks)
    return avg

result = average_marks(90, 85, 80, 95)
print("Average Marks:", result)

print("----------------------------")

# 🌟 Example 9: Nested Functions
def outer_function():
    print("Outer Function Called")

    def inner_function():
        print("Inner Function Executed")

    inner_function()

outer_function()

print("----------------------------")

# 🌟 Example 10: Practice Challenge
# Write a function to calculate total bill amount with tax and discount
def calculate_bill(amount, tax_rate=0.05, discount=0.10):
    tax = amount * tax_rate
    discount_amount = amount * discount
    final_amount = amount + tax - discount_amount
    return final_amount

bill = calculate_bill(1000)
print("Final Bill Amount (Default tax/discount): ₹", bill)

bill_custom = calculate_bill(2000, tax_rate=0.08, discount=0.15)
print("Final Bill Amount (Custom values): ₹", bill_custom)

print("\n✅ Day 8 completed successfully — you’ve mastered Python function parameters & defaults!")
