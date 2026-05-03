# Python Set Practice Questions


# Q1: Take a set of numbers as input and print it
s = set(map(int, input("Q1 Enter numbers: ").split()))
print("Set:", s)


# Q2: Find the length of the set
s = set(map(int, input("\nQ2 Enter numbers: ").split()))
print("Length:", len(s))


# Q3: Add an element to the set
s = set(map(int, input("\nQ3 Enter numbers: ").split()))
x = int(input("Enter element to add: "))
s.add(x)
print("Updated Set:", s)


# Q4: Remove an element from the set
s = set(map(int, input("\nQ4 Enter numbers: ").split()))
x = int(input("Enter element to remove: "))
s.discard(x)
print("Updated Set:", s)


# Q5: Check if an element exists in the set
s = set(map(int, input("\nQ5 Enter numbers: ").split()))
x = int(input("Enter element to check: "))
if x in s:
    print("Exists")
else:
    print("Not Exists")


# Q6: Perform union of two sets
a = set(map(int, input("\nQ6 Enter first set: ").split()))
b = set(map(int, input("Enter second set: ").split()))
print("Union:", a.union(b))


# Q7: Perform intersection of two sets
a = set(map(int, input("\nQ7 Enter first set: ").split()))
b = set(map(int, input("Enter second set: ").split()))
print("Intersection:", a.intersection(b))


# Q8: Find difference of two sets (a - b)
a = set(map(int, input("\nQ8 Enter first set: ").split()))
b = set(map(int, input("Enter second set: ").split()))
print("Difference:", a.difference(b))


# Q9: Check if one set is subset of another
a = set(map(int, input("\nQ9 Enter first set: ").split()))
b = set(map(int, input("Enter second set: ").split()))

if a.issubset(b):
    print("a is subset of b")
else:
    print("a is not subset of b")


# Q10: Remove duplicates from a list using set
lst = list(map(int, input("\nQ10 Enter list: ").split()))
unique = list(set(lst))
print("List without duplicates:", unique)
