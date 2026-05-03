# Python Identifier Rules 

# Valid Identifiers
name = "Rakheeb"
_age = 20
total_marks = 450
user2 = "Student"
PI = 3.14

print("Valid Identifiers:")
print(name, _age, total_marks, user2, PI)


# Invalid Identifiers (uncomment karoge toh error aayega)

# 2name = "Wrong"       # number se start nahi hota
# user-name = "Wrong"   # hyphen allowed nahi
# class = "Wrong"       # keyword use nahi kar sakte
# @value = 100          # special character allowed nahi


# Case Sensitivity
value = 10
Value = 20

print("\nCase Sensitive Check:")
print("value =", value)
print("Value =", Value)


# Keywords Check
import keyword

print("\nPython Keywords:")
print(keyword.kwlist)


# Naming Convention
user_name = "Rakheeb"
total_score = 95

print("\nBest Practice Variables:")
print(user_name, total_score)


# Mini Practice Task
test_name = input("\nEnter a variable name to check: ")

if test_name.isidentifier():
    print("Valid Identifier")
else:
    print("Invalid Identifier")
