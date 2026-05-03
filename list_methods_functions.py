# Python List Methods & Functions Practice


# Create list
lst = [10, 20, 30, 40, 20]
print("Original List:", lst)


# append()
lst.append(50)
print("\nAfter append:", lst)


# insert()
lst.insert(1, 15)
print("After insert:", lst)


# extend()
lst.extend([60, 70])
print("After extend:", lst)


# remove()
lst.remove(20)
print("After remove (first 20):", lst)


# pop()
lst.pop()
print("After pop:", lst)


# index()
print("\nIndex of 30:", lst.index(30))


# count()
print("Count of 20:", lst.count(20))


# sort()
lst.sort()
print("\nSorted List:", lst)


# reverse()
lst.reverse()
print("Reversed List:", lst)


# copy()
new_list = lst.copy()
print("\nCopied List:", new_list)


# clear()
temp = [1, 2, 3]
temp.clear()
print("After clear:", temp)


# Built-in functions
nums = [5, 2, 9, 1]

print("\nBuilt-in Functions:")
print("Length:", len(nums))
print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))


# Loop
print("\nLoop through list:")
for i in nums:
    print(i)


# Input list
user_list = list(map(int, input("\nEnter numbers: ").split()))
print("User List:", user_list)

print("Sorted:", sorted(user_list))   # returns new list
