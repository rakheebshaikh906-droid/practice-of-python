# Python Functions & Recursion Practice Questions


# Q1: Create a function to print "Hello World"
def greet():
    print("Hello World")

greet()


# Q2: Create a function to add two numbers and return result
def add(a, b):
    return a + b

print("\nAddition:", add(5, 3))


# Q3: Create a function to check even or odd
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print("\nEven/Odd:", even_odd(7))


# Q4: Create a function to find maximum of two numbers
def maximum(a, b):
    return a if a > b else b

print("\nMaximum:", maximum(10, 20))


# Q5: Create a function to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\nFactorial:", factorial(5))


# Q6: Create a function to print numbers from 1 to n using recursion
def print_n(n):
    if n == 0:
        return
    print_n(n - 1)
    print(n)

print("\nPrint 1 to n:")
print_n(5)


# Q7: Create a function to find sum of digits using recursion
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print("\nSum of digits:", sum_digits(1234))


# Q8: Create a function to reverse a string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print("\nReversed string:", reverse_string("python"))


# Q9: Create a function to calculate power (a^b) using recursion
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print("\nPower:", power(2, 4))


# Q10: Create a function to generate Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci series:")
for i in range(6):
    print(fibonacci(i))
