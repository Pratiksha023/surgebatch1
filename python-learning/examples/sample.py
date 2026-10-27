# this is a sample Python file
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# a = 1
# b = 2
# print(a,b)

# a = 1
# b = 2
# c = a + b
# print(c)


# x,y = input("Enter two values separated by a space: ").split()
# print(x, y)

# i =  int (input("how old are you "))
# f = float(input("how much do you weigh "))
# print(i, f)

# item_count = 4
# item_count += 2
# print(item_count)

# x = input("Enter a value: ")
# print ("you entered:" + x)

# y = input("Enter another value: ")
# print("you entered:" + y)

# x,y,z = input("Enter three values separated by a space: ").split()
# print("you entered:" + x)
# print("you entered:" + y)
# print("you entered:" + z)

# a = b = c = 10
# print(a, b, c)

# x = 10
# x = "abc"

# print(x)

#python operators
#operators: +, -, *, /, %, **, //
#operands : value on which the operator is applied

# arithmetic operators: +, -, *, /, %, **, //

# a = 10
# b = 5
# print("addition ", a + b)
# print("subtraction ", a - b)
# print("multiplication ", a * b)
# print("division ", a / b)
# print("modulus ", a % b)
# print("exponentiation ", a ** b)
# print("floor division ", a // b)

#comparison operators: ==, !=, >, <, >=, <=
# a = 10
# b = 5
# print("equal ", a == b)
# print("not equal ", a != b)
# print("greater than ", a > b)
# print("less than ", a < b)
# print("greater than or equal to ", a >= b)
# print("less than or equal to ", a <= b)

#bitwise operators: &, |, ^, ~, <<, >>
# a = 10
# b = 5
# print("bitwise AND ", a & b)
# print("bitwise OR ", a | b)
# print("bitwise XOR ", a ^ b)
# print("bitwise NOT ", ~a)
# print("left shift ", a << 1)
# print("right shift ", a >> 1)

# assignment operators: =, +=, -=, *=, /=, %=, **=, //=
# a = 10
# a += 5
# print("a after += 5 ", a)
# a -= 3
# print("a after -= 3 ", a)
# a *= 2
# print("a after *= 2 ", a)
# a /= 4
# print("a after /= 4 ", a)
# a %= 3
# print("a after %= 3 ", a)
# a **= 2
# print("a after **= 2 ", a)
# a //= 2
# print("a after //= 2 ", a)

#identity operators: is, is not
# a = 10
# b = 10
# print("a is b ", a is b)
# print("a is not b ", a is not b)

# membership operators: in, not in
# a = [1, 2, 3, 4, 5]
# print("2 in a ", 2 in a)
# print("6 not in a ", 6 not in a)

# ternary operator: value_if_true if condition else value_if_false
# a = 10
# result = "a is greater than 5" if a > 5 else "a is not greater than 5"
# print(result)


#datatypes

#numeric

#integer  a = 5
#float  f = 5.5
#complex  c = 2 + 3j


#dictionary  d = {"key": "value"}
#boolean  b = True
#string  s = "hello"
#list  l = [1, 2, 3]
#tuple  t = (1, 2, 3)
#set  s = {1, 2, 3}

#none  n = None


#condition statement
#if statement
# age = 20
# if age >= 18:
#     print("Eligible to vote.")

#if-else statement
    # if age >= 18:
    #     print("Eligible to vote.")
    # else:
    #     print("Not eligible to vote.")

#if-elif-else statement

    # if age < 13:
    #     print("Child")
    # elif age < 18:
    #     print("Teenager")
    # else:
    #     print("Adult")


#match statement
# value = 2
# match value:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case _:
#         print("Other")



#loops

#for loop
# for i in range(5):
#     print(i)

#while loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1

#function
# def greet(name):
#     print("Hello, " + name)

# greet("Alice")

#oop concepts
#class: blueprint for creating objects
#object: instance of a class
#encapsulation: bundling data and methods within a class
#inheritance: mechanism to create a new class from an existing class
#polymorphism: ability to take many forms, typically through method overriding

#class and object
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("Hello, my name is " + self.name)

# p = Person("Alice", 30)
# p.greet()

#inheritance example    
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("Animal sound")

# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

# d = Dog("Buddy")
# d.speak()

#polymorphism example
# class Cat(Animal):
#     def speak(self):
#         print("Meow!")

# c = Cat("Whiskers")
# c.speak()

#encapsulation example
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name

#     def get_age(self):
#         return self.__age

# p = Person("Alice", 30)
# print(p.get_name())
# print(p.get_age())

#data abstraction example
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name

#     def get_age(self):
#         return self.__age

# p = Person("Alice", 30)
# print(p.get_name())
# print(p.get_age())

#exception handling example

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except Exception as e:
#     print("An error occurred:", e)

#catch exception using try-except block example
# try:
#     x = int(input("Enter a number: "))
#     y = 10 / x
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Invalid input.")
# except Exception as e:
#     print("An error occurred:", e)


#multiple exception handling example

# a = ["10", "twenty", 30]
# try:
#     # 'twenty' cannot be converted to int
#     total = int(a[0]) + int(a[1])  
    
# except (ValueError, TypeError) as e:
#     print("Error", e)
    
# except IndexError:
#     print("Index out of range.")

#file handling example
#open("sample.txt", "r")
#close("sample.txt")

# try:
#     with open("sample.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found.")
# except Exception as e:
#     print("An error occurred:", e)

#reading and writing to a file example
#file.read() and file.write() methods are used to read from and write to a file respectively.

# try:
#     with open("sample.txt", "w") as file:
#         file.write("Hello, World!")
#     with open("sample.txt", "r") as file:
#         content = file.read()
#         print(content)
# except Exception as e:
#     print("An error occurred:", e)

#python database example
# import sqlite3

# try:
#     conn = sqlite3.connect("sample.db")
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
#     cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
#     conn.commit()
#     cursor.execute("SELECT * FROM users")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
# except Exception as e:
#     print("An error occurred:", e)
# finally:
#     conn.close()

#python package example (_init_.py)
# import math
# print(math.sqrt(16))