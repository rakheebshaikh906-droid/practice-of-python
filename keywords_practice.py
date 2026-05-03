# Python Keywords Practice

import keyword

# All Python keywords print karo
print("Python Keywords List:\n")
print(keyword.kwlist)


# Total number of keywords
print("\nTotal Keywords:", len(keyword.kwlist))


# Check if a word is keyword
word = input("\nEnter a word to check: ")

if keyword.iskeyword(word):
    print("Ye Python keyword hai (use nahi kar sakte as variable)")
else:
    print("Ye keyword nahi hai (use kar sakte ho variable ke liye)")
