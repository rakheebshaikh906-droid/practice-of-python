# Python Type Conversion Practice

# 1. Implicit Type Conversion (automatic)
a = 5       # int
b = 2.5     # float

result = a + b
print("Implicit Conversion Result:", result)
print("Type:", type(result))


# 2. Explicit Type Conversion (manual)

# int to float
x = 10
y = float(x)
print("\nint to float:", y)

# float to int
p = 5.9
q = int(p)
print("float to int:", q)

# int to string
num = 100
s = str(num)
print("int to string:", s, type(s))

# string to int
n = int("50")
print("string to int:", n + 10)


# 3. User Input Conversion
age = int(input("\nEnter your age: "))
print("Next year age:", age + 1)


# 4. Multiple Input Conversion
a, b = map(int, input("Enter two numbers: ").split())
print("Sum:", a + b)


# 5. Mini Practice Task
value = input("\nEnter a number: ")

# check type conversion safely
num = float(value)
print("Converted to float:", num)

if int(num) % 2 == 0:
    print("Even number")
else:
    print("Odd number")
