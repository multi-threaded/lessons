# Lesson 1: Python Variables, If-Else Statements, For Loops, and Lists

# 1. Variables
# Variables are used to store information that can be referenced and manipulated in a program.
# In Python, you can create a variable by simply assigning a value to it using the equals sign (=).

# Let's create a variable called 'name' and assign it a string value.
name = "Alice"  # This variable holds the name "Alice"

# We can also create a variable to hold a number.
age = 25  # This variable holds the number 25

# We can print the values of our variables to the console.
print("Name:", name)  # This will print: Name: Alice
print("Age:", age)    # This will print: Age: 25

# 2. If-Else Statements
# If-else statements are used to make decisions in your code.
# They allow you to execute certain blocks of code based on conditions.

# Let's check if the person is an adult or not.
if age >= 18:  # If the age is 18 or older
    print(name, "is an adult.")  # This will print if the condition is true
else:  # If the age is less than 18
    print(name, "is not an adult.")  # This will print if the condition is false

# 3. Lists
# A list is a collection of items that can be of different types. 
# Lists are ordered, changeable, and allow duplicate values.
# You can create a list by placing items inside square brackets [] and separating them with commas.

# Let's create a list of fruits.
fruits = ["apple", "banana", "cherry"]  # This is a list containing three fruit names

# We can print the entire list.
print("Fruits:", fruits)  # This will print: Fruits: ['apple', 'banana', 'cherry']

# We can access individual items in the list using their index (position).
# Note: List indexing starts at 0.
print("First fruit:", fruits[0])  # This will print: First fruit: apple
print("Second fruit:", fruits[1])  # This will print: Second fruit: banana

# 4. For Loops
# A for loop is used to iterate over a sequence (like a list or a range of numbers).
# It allows you to execute a block of code multiple times.

# Now, we will use a for loop to print each fruit in the list.
for fruit in fruits:  # For each fruit in the fruits list
    print("I like", fruit)  # This will print: I like apple, I like banana, I like cherry

# We can also use a for loop with the range function to repeat an action a specific number of times.
# The range function generates a sequence of numbers.
for i in range(5):  # This will loop 5 times (0 to 4)
    print("This is loop iteration number", i)  # This will print the current iteration number

# That's it for lesson 1! 
# You have learned about variables, if-else statements, lists, and for loops in Python.
