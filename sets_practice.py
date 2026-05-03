# Python Sets Practice


# Create set
s = {10, 20, 30, 40, 20}
print("Original Set:", s)   # duplicates automatically remove


# Add element
s.add(50)
print("\nAfter add:", s)


# Update (multiple elements add)
s.update([60, 70])
print("After update:", s)


# Remove element
s.remove(20)
print("\nAfter remove:", s)


# Discard (no error if not present)
s.discard(100)
print("After discard:", s)


# Pop (random element remove)
s.pop()
print("\nAfter pop:", s)


# Length
print("\nLength:", len(s))


# Membership check
print("\nCheck 30 in set:", 30 in s)


# Loop
print("\nLoop through set:")
for item in s:
    print(item)


# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("\nUnion:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference (a - b):", a.difference(b))
print("Symmetric Difference:", a.symmetric_difference(b))


# Copy
new_set = s.copy()
print("\nCopied Set:", new_set)


# Clear
temp = {1, 2, 3}
temp.clear()
print("After clear:", temp)


# Convert list to set
lst = [1, 2, 2, 3, 4]
set_from_list = set(lst)
print("\nList to Set:", set_from_list)


# Input set
user_set = set(map(int, input("\nEnter numbers: ").split()))
print("User Set:", user_set)
