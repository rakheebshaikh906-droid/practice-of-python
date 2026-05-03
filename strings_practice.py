# Python Strings Practice


# Q1: Take a string input and print it
s = input("Q1 Enter a string: ")
print("You entered:", s)


# Q2: Print length of a string
text = input("\nQ2 Enter a string: ")
print("Length:", len(text))


# Q3: Convert string to uppercase and lowercase
text = input("\nQ3 Enter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())


# Q4: Check if a substring exists
text = input("\nQ4 Enter a string: ")
sub = input("Enter substring to check: ")

if sub in text:
    print("Substring found")
else:
    print("Substring not found")


# Q5: Count number of vowels in a string
text = input("\nQ5 Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowel count:", count)


# Q6: Reverse a string
text = input("\nQ6 Enter a string: ")
print("Reversed:", text[::-1])


# Q7: Check palindrome
text = input("\nQ7 Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Q8: Replace a word in string
text = input("\nQ8 Enter a string: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")

print("Updated string:", text.replace(old, new))


# Q9: Remove spaces from string
text = input("\nQ9 Enter a string: ")
print("Without spaces:", text.replace(" ", ""))


# Q10: Split string into words
text = input("\nQ10 Enter a sentence: ")
words = text.split()
print("Words list:", words)
