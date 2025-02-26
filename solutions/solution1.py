# Create a list of fruits
fruits = ["apple", "banana", "cherry", "orange", "grape"]

# Ask the user to input the name of a fruit
user_fruit = input("Enter the name of a fruit: ")

# Check if the fruit is in the list
if user_fruit in fruits:
    print(user_fruit, "is available!")
else:
    print(user_fruit, "is not available.")

# Print each fruit in the list
for fruit in fruits:
    print("Available fruit:", fruit)