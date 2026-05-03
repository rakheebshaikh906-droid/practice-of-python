# Python File Input/Output Practice


# Write to file (overwrite)
with open("sample.txt", "w") as f:
    f.write("Hello Rakheeb\n")
    f.write("Learning Python File Handling\n")


# Read full file
with open("sample.txt", "r") as f:
    content = f.read()
    print("Read full file:\n", content)


# Read line by line
with open("sample.txt", "r") as f:
    print("Read line by line:")
    for line in f:
        print(line.strip())


# Append to file
with open("sample.txt", "a") as f:
    f.write("This is appended line\n")


# Read after append
with open("sample.txt", "r") as f:
    print("\nAfter append:\n", f.read())


# Read first n characters
with open("sample.txt", "r") as f:
    print("First 10 characters:", f.read(10))


# File exists check
import os

if os.path.exists("sample.txt"):
    print("\nFile exists")
else:
    print("File does not exist")


# Rename file
os.rename("sample.txt", "new_sample.txt")
print("File renamed")


# Delete file
os.remove("new_sample.txt")
print("File deleted")
