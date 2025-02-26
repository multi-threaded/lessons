# Lesson 2: Functions, Dictionaries, and While Loops

# 1. Functions
# Functions are reusable blocks of code that perform a specific task.
# They help organize code and make it more modular, allowing you to call the same code multiple times.

# Defining a Function
def greet(name):  # 'name' is a parameter that the function takes
    """
    This function takes a name as input and prints a greeting.
    """
    print("Hello,", name)  # This line will print a greeting

# Calling the Function
greet("Alice")  # This will print: Hello, Alice
greet("Bob")    # This will print: Hello, Bob

# Functions can also return values. Let's define a function that adds two numbers.
def add_numbers(a, b):  # 'a' and 'b' are parameters
    """
    This function takes two numbers and returns their sum.
    """
    return a + b  # This line returns the sum of a and b

# Calling the Function and Storing the Result
result = add_numbers(5, 3)  # This will return 8
print("The sum is:", result)  # This will print: The sum is: 8

# 2. Dictionaries
# A dictionary is a collection of key-value pairs. It is unordered, changeable, and indexed.
# You can think of a dictionary as a real-life dictionary where you look up a word (key) to find its definition (value).

# Creating a Dictionary
person = {
    "name": "Alice",  # Key: "name", Value: "Alice"
    "age": 25,        # Key: "age", Value: 25
    "city": "New York"  # Key: "city", Value: "New York"
}

# Printing the Entire Dictionary
print("Person:", person)  # This will print the dictionary

# Accessing Values Using Keys
print("Name:", person["name"])  # This will print: Name: Alice
print("Age:", person["age"])    # This will print: Age: 25

# Modifying the Dictionary
# Adding a new key-value pair to the dictionary.
person["job"] = "Engineer"  # Adding a new key "job" with value "Engineer"
print("Updated Person:", person)  # This will print the updated dictionary

# Updating an existing value
person["age"] = 26  # Changing the age from 25 to 26
print("Updated Age:", person["age"])  # This will print: Updated Age: 26

# Removing a key-value pair
del person["city"]  # This will remove the key "city" from the dictionary
print("Person after removing city:", person)  # This will print the dictionary without the city

# 3. While Loops
# A while loop repeatedly executes a block of code as long as a specified condition is true.
# It is useful when you do not know in advance how many times you need to iterate.

# Using a While Loop
count = 1  # Initialize a variable to keep track of the count
while count <= 5:  # As long as count is less than or equal to 5
    print("Count is:", count)  # Print the current count
    count += 1  # Increment the count by 1

# Example of a While Loop with User Input
# Let's create a simple program that asks the user to enter a number until they enter 0.
user_input = -1  # Initialize user_input to a value that is not 0
while user_input != 0:  # Continue looping until the user enters 0
    user_input = int(input("Enter a number (0 to exit): "))  # Get user input and convert it to an integer
    print("You entered:", user_input)  # Print the entered number

# That's it for Lesson 2!
# You have learned about functions, dictionaries, and while loops in Python.
