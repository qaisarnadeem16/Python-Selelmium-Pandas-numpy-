# If else condition
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

    # For loops in python
LitMe = ["Harry", "Patrick", "Tyler"]

for fruit in LitMe:
     print(fruit)

# While loop
count = 0

while count < 5:
    print("Count:", count)
    count += 1

# Break Statement
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        break
    print(number)

# Continue Statement
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        continue
    print(number)

# Short hand if-else statement
x = 5

result = "Even" if x % 2 == 0 else "Odd"
print(result)

# Functions in Python
import math


def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area


circle_radius = 3
area = calculate_circle_area(circle_radius)
print("The area of the circle is:", area)

# Lambda functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Global variable
count = 0


def increment():
    global count  # Declare the variable as global to modify it within the function
    count += 1


def main():
    print("Initial count:", count)
    increment()
    print("Updated count:", count)


main()

# f.string and string formatting
name = "Harry"
age = 23
height = 5.10
# F-string formatting
greeting = f"Hello, my name is {name}."
info = f"I am {age} years old and my height is {height:.2f} feet."
# Traditional string formatting
greeting_formatted = "Hello, my name is {}.".format(name)
info_formatted = "I am {} years old and my height is {:.2f} feet.".format(age, height)
print(greeting)
print(info)
print(greeting_formatted)
print(info_formatted)
