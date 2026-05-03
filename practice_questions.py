# Python Practice Questions (Variables + Input + Operators + Condition + Type Conversion)


# Q1: Take user's name as input and print "Hello <name>"
name = input("Q1 Enter your name: ")
print("Hello", name)


# Q2: Take age as input and print next year's age
age = int(input("\nQ2 Enter your age: "))
print("Next year age:", age + 1)


# Q3: Take two numbers as input and print their sum
a = int(input("\nQ3 Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)


# Q4: Take a number and check whether it is even or odd
num = int(input("\nQ4 Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q5: Take two numbers and print the greater number
x = int(input("\nQ5 Enter first number: "))
y = int(input("Enter second number: "))
if x > y:
    print("Greater:", x)
else:
    print("Greater:", y)


# Q6: Take marks as input and print grade
marks = int(input("\nQ6 Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# Q7: Take two numbers in one line and print multiplication
a, b = map(int, input("\nQ7 Enter two numbers: ").split())
print("Multiplication:", a * b)


# Q8: Take temperature (float) and check if it is greater than 30
temp = float(input("\nQ8 Enter temperature: "))
if temp > 30:
    print("Hot")
else:
    print("Normal")


# Q9: Take a number as string, convert to int and add 10
s = input("\nQ9 Enter a number in string: ")
num = int(s)
print("After adding 10:", num + 10)


# Q10: Take three numbers and print the largest
a, b, c = map(int, input("\nQ10 Enter three numbers: ").split())

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
