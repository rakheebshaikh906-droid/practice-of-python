# Python Tuples Practice


# Create tuple
t = (10, 20, 30, 40, 20)
print("Original Tuple:", t)


# Access elements
print("\nFirst element:", t[0])
print("Last element:", t[-1])


# Slicing
print("\nFirst 3 elements:", t[:3])
print("Last 2 elements:", t[-2:])


# Tuple is immutable (cannot change)
# t[1] = 25   # ❌ error


# Count
print("\nCount of 20:", t.count(20))


# Index
print("Index of 30:", t.index(30))


# Length
print("\nLength:", len(t))


# Loop
print("\nLooping through tuple:")
for item in t:
    print(item)


# Mixed data types
mixed = (10, "Hello", 3.5, True)
print("\nMixed Tuple:", mixed)


# Single element tuple
single = (5,)
print("\nSingle element tuple:", single)


# Tuple unpacking
a, b, c = (1, 2, 3)
print("\nUnpacked values:", a, b, c)


# Convert list to tuple
lst = [100, 200, 300]
t2 = tuple(lst)
print("\nList to Tuple:", t2)


# Convert tuple to list
t3 = (7, 8, 9)
lst2 = list(t3)
print("Tuple to List:", lst2)


# Input tuple
user_tuple = tuple(map(int, input("\nEnter numbers: ").split()))
print("User Tuple:", user_tuple)


# Built-in functions
print("\nMax:", max(user_tuple))
print("Min:", min(user_tuple))
print("Sum:", sum(user_tuple))
