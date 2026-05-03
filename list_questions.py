# Python List Practice Questions


# Q1: Take a list of numbers as input and print it
lst = list(map(int, input("Q1 Enter numbers: ").split()))
print("List:", lst)


# Q2: Print the sum of all elements in the list
lst = list(map(int, input("\nQ2 Enter numbers: ").split()))
print("Sum:", sum(lst))


# Q3: Find the maximum and minimum element in the list
lst = list(map(int, input("\nQ3 Enter numbers: ").split()))
print("Max:", max(lst))
print("Min:", min(lst))


# Q4: Count how many times a number appears in the list
lst = list(map(int, input("\nQ4 Enter numbers: ").split()))
x = int(input("Enter number to count: "))
print("Count:", lst.count(x))


# Q5: Reverse the list
lst = list(map(int, input("\nQ5 Enter numbers: ").split()))
print("Reversed:", lst[::-1])


# Q6: Sort the list in ascending order
lst = list(map(int, input("\nQ6 Enter numbers: ").split()))
lst.sort()
print("Sorted:", lst)


# Q7: Remove duplicates from the list
lst = list(map(int, input("\nQ7 Enter numbers: ").split()))
unique = list(set(lst))
print("Without duplicates:", unique)


# Q8: Find the second largest element in the list
lst = list(map(int, input("\nQ8 Enter numbers: ").split()))
lst = list(set(lst))
lst.sort()
print("Second largest:", lst[-2])


# Q9: Check if a number exists in the list
lst = list(map(int, input("\nQ9 Enter numbers: ").split()))
x = int(input("Enter number to check: "))

if x in lst:
    print("Exists")
else:
    print("Not Exists")


# Q10: Merge two lists
lst1 = list(map(int, input("\nQ10 Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))

merged = lst1 + lst2
print("Merged List:", merged)
