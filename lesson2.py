# Lesson 2: Functions, Dictionaries, and While Loops

# 1. Functions
# Functions are reusable blocks of code that perform a specific task.

# Let's define a function that greets a person.
def greet(name):  # 'name' is a parameter
    print("Hello,", name)  # This line will print a greeting

# Now we can call the function with different names.
greet("Alice")  # This will print: Hello, Alice
greet("Bob")    # This will print: Hello, Bob

# Let's define a function that adds two numbers and returns the result.
def add_numbers(a, b):  # 'a' and 'b' are parameters
    return a + b  # This line returns the sum of a and b

# We can call the function and store the result in a variable.
result = add_numbers(5, 3)  # This will return 8
print("The sum is:", result)  # This will print: The sum is: 8

# 2. Dictionaries
# A dictionary is a collection of key-value pairs.

# Let's create a dictionary to store information about a person.
person = {
    "name": "Alice",  # Key: "name", Value: "Alice"
    "age": 25,        # Key: "age", Value: 25
    "city": "New York"  # Key: "city", Value: "New York"
}

# We can print the entire dictionary.
print("Person:", person)  # This will print the dictionary

# We can access values using their keys.
print("Name:", person["name"])  # This will print: Name: Alice
print("Age:", person["age"])    # This will print: Age: 25

# We can add a new key-value pair to the dictionary.
person["job"] = "Engineer"  # Adding a new key "job" with value "Engineer"
print("Updated Person:", person)  # This will print the updated dictionary

# 3. While Loops
# A while loop repeatedly executes a block of code as long as a specified condition is true.

# Let's use a while loop to count from 1 to 5.
count = 1  # Initialize a variable to keep track of the count
while count <= 5:  # As long as count is less than or equal to 5
    print("Count is:", count)  # Print the current count
    count += 1  # Increment the count by 1

# That's it for Lesson 2!
# You have learned about functions, dictionaries, and while loops in Python.
