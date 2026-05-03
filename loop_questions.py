# Python Loop Practice Questions


# Q1: Print numbers from 1 to n
n = int(input("Q1 Enter n: "))
for i in range(1, n + 1):
    print(i)


# Q2: Print even numbers from 1 to n
n = int(input("\nQ2 Enter n: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)


# Q3: Find sum of numbers from 1 to n
n = int(input("\nQ3 Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)


# Q4: Print multiplication table of a number
n = int(input("\nQ4 Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# Q5: Reverse a number using while loop
num = int(input("\nQ5 Enter number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed:", rev)


# Q6: Count digits in a number
num = int(input("\nQ6 Enter number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digits:", count)


# Q7: Check if a number is prime
n = int(input("\nQ7 Enter number: "))
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")


# Q8: Print factorial of a number
n = int(input("\nQ8 Enter number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)


# Q9: Print this pattern
# *
# **
# ***
# ****
n = int(input("\nQ9 Enter rows: "))
for i in range(1, n + 1):
    print("*" * i)


# Q10: Find sum of digits of a number
num = int(input("\nQ10 Enter number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)
