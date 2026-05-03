# Python Lists Practice


# Create list
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)


# Access elements
print("\nFirst element:", numbers[0])
print("Last element:", numbers[-1])


# Slicing
print("\nFirst 3 elements:", numbers[:3])
print("Last 2 elements:", numbers[-2:])


# Update element
numbers[1] = 25
print("\nAfter update:", numbers)


# Add elements
numbers.append(60)
print("\nAfter append:", numbers)

numbers.insert(2, 15)
print("After insert:", numbers)


# Remove elements
numbers.remove(30)
print("\nAfter remove:", numbers)

numbers.pop()
print("After pop:", numbers)


# Length
print("\nLength:", len(numbers))


# Sort
numbers.sort()
print("\nSorted List:", numbers)


# Reverse
numbers.reverse()
print("Reversed List:", numbers)


# Count
print("\nCount of 25:", numbers.count(25))


# Index
print("Index of 25:", numbers.index(25))


# Loop through list
print("\nLooping through list:")
for num in numbers:
    print(num)


# List with different data types
mixed = [10, "Hello", 3.5, True]
print("\nMixed List:", mixed)


# Input list
user_list = list(map(int, input("\nEnter numbers separated by space: ").split()))
print("User List:", user_list)


# Sum of list
print("Sum:", sum(user_list))


# Max and Min
print("Max:", max(user_list))
print("Min:", min(user_list))
