# Python Operators Practice - Clean Version

# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# Comparison Operators
x = 5
y = 10

print("\nComparison Operators:")
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# Logical Operators
p = True
q = False

print("\nLogical Operators:")
print(p and q)
print(p or q)
print(not p)


# Assignment Operators
num = 10

print("\nAssignment Operators:")
num += 5
print("num += 5 ->", num)

num -= 3
print("num -= 3 ->", num)

num *= 2
print("num *= 2 ->", num)

num /= 4
print("num /= 4 ->", num)


# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nIdentity Operators:")
print(a is b)
print(a is c)
print(a is not c)


# Membership Operators
list1 = [10, 20, 30]

print("\nMembership Operators:")
print(10 in list1)
print(50 not in list1)


# Mini Practice Task
num = int(input("\nEnter a number: "))

if num % 2 == 0 and num > 0:
    print("Positive Even Number")
else:
    print("Either Odd or Negative")
