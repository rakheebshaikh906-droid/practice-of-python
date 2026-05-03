# Python Set Methods & Functions Practice


# Create set
s = {10, 20, 30, 40}
print("Original Set:", s)


# add()
s.add(50)
print("\nAfter add:", s)


# update()
s.update([60, 70])
print("After update:", s)


# remove()
s.remove(20)
print("\nAfter remove:", s)


# discard()
s.discard(100)   # no error if not present
print("After discard:", s)


# pop()
s.pop()   # removes random element
print("\nAfter pop:", s)


# copy()
new_set = s.copy()
print("\nCopied Set:", new_set)


# clear()
temp = {1, 2, 3}
temp.clear()
print("After clear:", temp)


# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\nUnion:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference (a - b):", a.difference(b))
print("Symmetric Difference:", a.symmetric_difference(b))


# Subset / Superset
x = {1, 2}
y = {1, 2, 3, 4}

print("\nIs subset:", x.issubset(y))
print("Is superset:", y.issuperset(x))


# Disjoint
print("Is disjoint:", x.isdisjoint({5, 6}))


# Built-in functions
nums = {5, 2, 9, 1}

print("\nBuilt-in Functions:")
print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))


# Loop
print("\nLoop through set:")
for i in nums:
    print(i)


# Input set
user_set = set(map(int, input("\nEnter numbers: ").split()))
print("User Set:", user_set)


# Sorted (returns list)
print("Sorted:", sorted(user_set))
