# Python Conditional Statements Practice

# 1. Simple if
num = 10

if num > 5:
    print("Number is greater than 5")


# 2. if-else
age = int(input("\nEnter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# 3. if-elif-else
marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 4. Nested if
num = int(input("\nEnter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Number is Negative or Zero")


# 5. Short Hand if (one line)
x = 20

if x > 10: print("x is greater than 10")


# 6. Short Hand if-else (ternary)
y = 5

result = "Even" if y % 2 == 0 else "Odd"
print("\nTernary Result:", result)


# 7. Logical Operators with if
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

if a > 0 and b > 0:
    print("Both numbers are positive")
else:
    print("At least one number is not positive")
