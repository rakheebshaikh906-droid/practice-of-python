# Python Input Practice - GitHub Codespaces Ready

# 1. Simple Input
name = input("Enter your name: ")
print("Hello", name)


# 2. Number Input (important)
age = int(input("Enter your age: "))
print("Next year age:", age + 1)


# 3. Float Input
height = float(input("Enter your height: "))
print("Your height is:", height)


# 4. Multiple Inputs (same line)
a, b = input("Enter two numbers separated by space: ").split()

a = int(a)
b = int(b)

print("Sum:", a + b)


# 5. Direct Convert (shortcut)
x, y = map(int, input("Enter two numbers: ").split())
print("Multiplication:", x * y)


# 6. Mini Practice Task
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
