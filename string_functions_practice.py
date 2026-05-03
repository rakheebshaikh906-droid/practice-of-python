# Python String Functions Practice


text = "Hello World Python"

print("Original:", text)


# Uppercase & Lowercase
print("\nUppercase:", text.upper())
print("Lowercase:", text.lower())


# Length
print("\nLength:", len(text))


# Count
print("\nCount of 'o':", text.count("o"))


# Find
print("\nIndex of 'World':", text.find("World"))


# Replace
print("\nReplace 'World' with 'Rakheeb':", text.replace("World", "Rakheeb"))


# Split
words = text.split()
print("\nSplit:", words)


# Join
joined = "-".join(words)
print("Joined:", joined)


# Startswith / Endswith
print("\nStarts with 'Hello':", text.startswith("Hello"))
print("Ends with 'Python':", text.endswith("Python"))


# Strip
text2 = "   Hello   "
print("\nBefore strip:", text2)
print("After strip:", text2.strip())


# Slicing
print("\nFirst 5 characters:", text[:5])
print("Last 6 characters:", text[-6:])


# Reverse string
print("\nReversed:", text[::-1])


# Input Example
user_text = input("\nEnter a string: ")

print("Upper:", user_text.upper())
print("Lower:", user_text.lower())
print("Length:", len(user_text))
print("Reversed:", user_text[::-1])
