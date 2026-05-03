# Python Loops Practice (Clean Code)


# Basic for loop
print("For Loop:")
for i in range(5):
    print(i)


# Range with start and end
print("\nRange (1 to 5):")
for i in range(1, 6):
    print(i)


# Range with step
print("\nRange with step (even numbers):")
for i in range(0, 10, 2):
    print(i)


# While loop
print("\nWhile Loop:")
i = 1
while i <= 5:
    print(i)
    i += 1


# Loop through string
text = "Python"
print("\nString Loop:")
for ch in text:
    print(ch)


# Loop through list
lst = [10, 20, 30, 40]
print("\nList Loop:")
for num in lst:
    print(num)


# Break example
print("\nBreak:")
for i in range(10):
    if i == 5:
        break
    print(i)


# Continue example
print("\nContinue:")
for i in range(5):
    if i == 2:
        continue
    print(i)


# Nested loop
print("\nNested Loop:")
for i in range(3):
    for j in range(3):
        print(i, j)


# Pattern printing
print("\nPattern:")
for i in range(1, 5):
    print("*" * i)


# Reverse loop
print("\nReverse Loop:")
for i in range(5, 0, -1):
    print(i)


# Sum using loop
n = 5
total = 0
for i in range(1, n + 1):
    total += i
print("\nSum:", total)


# Input based loop
n = int(input("\nEnter a number: "))
for i in range(1, n + 1):
    print(i)
