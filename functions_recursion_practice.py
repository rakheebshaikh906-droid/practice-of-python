# Python Functions & Recursion Practice


# Simple function
def greet():
    print("Hello Rakheeb")

greet()


# Function with parameters
def add(a, b):
    return a + b

print("\nAddition:", add(10, 5))


# Function with default parameter
def power(base, exp=2):
    return base ** exp

print("\nPower:", power(3))
print("Power (custom):", power(3, 3))


# Function returning multiple values
def calc(a, b):
    return a + b, a - b, a * b

sum_val, diff, prod = calc(10, 5)
print("\nMultiple return:", sum_val, diff, prod)


# Function with list
def list_sum(lst):
    return sum(lst)

print("\nList Sum:", list_sum([1, 2, 3, 4]))


# Lambda function
square = lambda x: x * x
print("\nLambda square:", square(5))


# Recursion - factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\nFactorial:", factorial(5))


# Recursion - fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci (0 to 5):")
for i in range(6):
    print(fibonacci(i))


# Recursion - sum of numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print("\nSum using recursion:", sum_n(5))


# Input based function
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("\nEnter a number: "))
print("Result:", even_odd(num))
