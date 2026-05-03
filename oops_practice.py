# Python OOPs Practice


# Class and Object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name, "Age:", self.age)


s1 = Student("Rakheeb", 20)
s1.display()


# Encapsulation (private variable)
class Account:
    def __init__(self, balance):
        self.__balance = balance   # private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount


acc = Account(1000)
acc.deposit(500)
print("\nBalance:", acc.get_balance())


# Inheritance
class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()
d.sound()
d.bark()


# Polymorphism
class Bird:
    def speak(self):
        print("Bird speaks")


class Parrot(Bird):
    def speak(self):
        print("Parrot talks")


class Sparrow(Bird):
    def speak(self):
        print("Sparrow chirps")


print("\nPolymorphism:")
for b in [Parrot(), Sparrow()]:
    b.speak()


# Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


c = Circle(5)
print("\nCircle Area:", c.area())


# Constructor & Destructor
class Demo:
    def __init__(self):
        print("\nConstructor called")

    def __del__(self):
        print("Destructor called")


obj = Demo()
del obj


# Class variable vs Instance variable
class Test:
    class_var = 100   # class variable

    def __init__(self, val):
        self.instance_var = val


t1 = Test(10)
t2 = Test(20)

print("\nClass Var:", t1.class_var, t2.class_var)
print("Instance Var:", t1.instance_var, t2.instance_var)


# Static method
class Math:
    @staticmethod
    def add(a, b):
        return a + b


print("\nStatic Method:", Math.add(5, 3))


# Class method
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


c1 = Counter()
c2 = Counter()
print("Object Count:", Counter.get_count())
