# Lesson 3: Classes and Objects, Exception Handling, and File I/O

# 1. Classes and Objects
# Classes are a way to create your own data types in Python. 
# An object is an instance of a class. Classes encapsulate data (attributes) and functions (methods) that operate on that data.

# Defining a Class
class Dog:
    # The __init__ method is a special method called a constructor. 
    # It is automatically called when you create a new instance of the class.
    def __init__(self, name, age):  # 'name' and 'age' are parameters that we will use to initialize the object
        self.name = name  # 'self.name' is an attribute of the class. It stores the name of the dog.
        self.age = age    # 'self.age' is another attribute that stores the age of the dog.

    # This method makes the dog bark.
    def bark(self):  
        print(self.name, "says: Woof!")  # This prints a message that includes the dog's name and a bark sound.

    # This method calculates the dog's age in human years.
    def get_human_years(self):  
        return self.age * 7  # This assumes that 1 dog year is equivalent to 7 human years.

# Creating an Object
my_dog = Dog("Buddy", 3)  # Here, we create an instance of the Dog class named 'my_dog' with the name "Buddy" and age 3.
my_dog.bark()  # This calls the bark method on the my_dog object, which will print: Buddy says: Woof!
print("Buddy's age in human years is:", my_dog.get_human_years())  # This calls the get_human_years method and prints the result.

# 2. Exception Handling
# Exception handling allows you to manage errors gracefully in your code.
# You can use try and except blocks to catch and handle exceptions.

# Example of Exception Handling
try:
    # Trying to convert a string to an integer
    number = int(input("Enter a number: "))  # This line prompts the user to enter a number and tries to convert it to an integer.
    print("You entered:", number)  # If successful, it prints the number entered by the user.
except ValueError:  # This block will execute if a ValueError occurs (e.g., if the user enters a non-numeric value).
    print("That's not a valid number!")  # Inform the user that the input was invalid.

# 3. File I/O
# File I/O (Input/Output) allows you to read from and write to files.

# Writing to a File
with open("example.txt", "w") as file:  # The 'open' function is used to open a file. "example.txt" is the name of the file, and "w" means we want to write to it.
    file.write("Hello, World!\n")  # This line writes the string "Hello, World!" to the file, followed by a newline character.
    file.write("This is a file I/O example.\n")  # This line writes another string to the file.

# Reading from a File
with open("example.txt", "r") as file:  # Here, we open the same file in read mode ("r").
    content = file.read()  # This reads the entire content of the file and stores it in the variable 'content'.
    print("File Content:\n", content)  # This prints the content of the file to the console.

# That's it for Lesson 3!
# You have learned about classes and objects, exception handling, and file I/O in Python.