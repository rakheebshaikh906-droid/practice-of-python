# Python Loops Practice (For + While)


# For loop
print("For Loop:")
for i in range(5):
    print(i)


# Range with start and end
print("\nRange (1 to 5):")
for i in range(1, 6):
    print(i)


# Range with step
print("\nEven Numbers:")
for i in range(0, 10, 2):
    print(i)


# While loop (basic)
print("\nWhile Loop:")
i = 1
while i <= 5:
    print(i)
    i += 1


# While loop (reverse)
print("\nWhile Reverse:")
i = 5
while i > 0:
    print(i)
    i -= 1


# While loop (sum)
print("\nWhile Sum:")
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Sum:", total)


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


# Break (for loop)
print("\nBreak:")
for i in range(10):
    if i == 5:
        break
    print(i)


# Continue (for loop)
print("\nContinue:")
for i in range(5):
    if i == 2:
        continue
    print(i)


# Break (while loop)
print("\nWhile Break:")
i = 1
while True:
    if i == 5:
        break
    print(i)
    i += 1


# Continue (while loop)
print("\nWhile Continue:")
i = 0
while i < 5:
    i += 1
    if i == 3:
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


# Input based while loop
print("\nInput Loop:")
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i += 1
