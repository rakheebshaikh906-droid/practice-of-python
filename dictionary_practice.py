# Python Dictionary Practice


# Create dictionary
student = {
    "name": "Rakheeb",
    "age": 20,
    "marks": 85
}

print("Original Dictionary:", student)


# Access values
print("\nName:", student["name"])
print("Age:", student.get("age"))


# Add new key-value
student["city"] = "Nagpur"
print("\nAfter adding city:", student)


# Update value
student["marks"] = 90
print("After updating marks:", student)


# Remove element
student.pop("age")
print("\nAfter pop age:", student)


# Remove last item
student.popitem()
print("After popitem:", student)


# Keys, Values, Items
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# Loop through dictionary
print("\nLoop through dictionary:")
for key, value in student.items():
    print(key, ":", value)


# Check key exists
print("\nCheck key exists:")
print("name" in student)


# Length
print("\nLength:", len(student))


# Copy dictionary
new_student = student.copy()
print("\nCopied Dictionary:", new_student)


# Clear dictionary
temp = {"a": 1, "b": 2}
temp.clear()
print("After clear:", temp)


# Nested dictionary
data = {
    "student1": {"name": "A", "marks": 80},
    "student2": {"name": "B", "marks": 90}
}
print("\nNested Dictionary:", data)


# Input dictionary
n = int(input("\nEnter number of items: "))
user_dict = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

print("User Dictionary:", user_dict)
