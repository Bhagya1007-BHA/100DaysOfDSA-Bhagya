# Day 5: Loops in Python

# 🌟 Example 1: Using a for loop with a list
fruits = ["apple", "banana", "mango", "grapes"]
print("For Loop Example:")
for fruit in fruits:
    print(f"I like {fruit}")
print("----------------------------")

# 🌟 Example 2: Using range() in for loop
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)
print("----------------------------")

# 🌟 Example 3: Printing even numbers between 1 to 10
print("Even Numbers:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
print("----------------------------")

# 🌟 Example 4: While loop example
count = 1
print("While Loop Example:")
while count <= 5:
    print("Count:", count)
    count += 1
print("----------------------------")

# 🌟 Example 5: Using break statement
print("Break Statement Example:")
for i in range(1, 10):
    if i == 5:
        print("Loop stopped at", i)
        break
    print(i)
print("----------------------------")

# 🌟 Example 6: Using continue statement
print("Continue Statement Example:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Value:", i)
print("----------------------------")

# 🌟 Example 7: Nested for loop (Multiplication table)
print("Multiplication Table (1 to 5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # new line after each row
print("----------------------------")

# 🌟 Example 8: Using else with loop
for i in range(1, 4):
    print("Iteration:", i)
else:
    print("Loop Completed Successfully!")
print("----------------------------")

