# Python Variables Practice 

# 1. Basic Variables
name = "Rakheeb"
age = 20
height = 5.8
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)


# 2. Multiple Assignment
a, b, c = 10, 20, 30
print("\nMultiple Values:", a, b, c)


# 3. Same Value Assignment
x = y = z = 100
print("Same Values:", x, y, z)


# 4. Type Checking
print("\nData Types:")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# 5. User Input (important for practice)
user_name = input("\nEnter your name: ")
user_age = int(input("Enter your age: "))

print("Hello", user_name)
print("Next year age:", user_age + 1)


# 6. Arithmetic Operations
num1 = 15
num2 = 4

print("\nArithmetic Operations:")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)


# 7. String Operations
first = "Hello"
second = "World"

print("\nString Operations:")
print(first + " " + second)
print(first * 3)


# 8. Variable Update
score = 50
print("\nOriginal Score:", score)

score += 10
print("Updated Score:", score)


# 9. Constants (Convention)
PI = 3.14159
print("\nConstant PI:", PI)


# 10. Mini Practice Task
# Swap two variables
a = 5
b = 10

print("\nBefore Swap:", a, b)
a, b = b, a
print("After Swap:", a, b)
