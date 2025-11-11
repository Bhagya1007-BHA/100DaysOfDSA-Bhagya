# Day 6: Break, Continue, and Pass Statements in Python

# 🌟 Example 1: Break Statement
# Used to stop the loop completely when a condition is met
print("Break Statement Example:")
for i in range(1, 11):
    if i == 6:
        print("Breaking the loop at i =", i)
        break
    print("Current value of i:", i)
print("Loop ended using break.\n")

print("----------------------------")

# 🌟 Example 2: Continue Statement
# Skips the current iteration and continues with the next one
print("Continue Statement Example:")
for i in range(1, 8):
    if i == 4:
        print("Skipping value 4")
        continue
    print("Value:", i)
print("Loop completed using continue.\n")

print("----------------------------")

# 🌟 Example 3: Pass Statement
# Used as a placeholder for code that is not yet implemented
print("Pass Statement Example:")
for i in range(1, 6):
    if i == 3:
        pass  # No operation; used to avoid syntax error
        print("Pass statement executed (no operation)")
    else:
        print("Value:", i)
print("Loop completed using pass.\n")

print("----------------------------")

# 🌟 Example 4: Using all three in nested loops
print("Nested Loop Example with break, continue, pass:")
for i in range(1, 4):
    for j in range(1, 6):
        if j == 2:
            print(f"Continue inner loop at j={j}")
            continue
        elif j == 4:
            print(f"Break inner loop at j={j}")
            break
        elif j == 3:
            pass  # just to show placeholder usage
        print(f"i={i}, j={j}")
    print("End of inner loop iteration for i =", i)
print("Program completed successfully ✅")
