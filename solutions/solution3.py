class Pet:
    """A class to represent a pet."""

    def __init__(self, name, age, species):
        """Initialize a new instance of the Pet class."""
        self.name = name  # Set the pet's name
        self.age = age    # Set the pet's age
        self.species = species  # Set the pet's species

    def bark(self):
        """Print a sound that the pet makes based on its species."""
        if self.species.lower() == "dog":
            print(f"{self.name} says: Woof!")  # Dog sound
        elif self.species.lower() == "cat":
            print(f"{self.name} says: Meow!")  # Cat sound
        else:
            print(f"{self.name} makes a sound.")  # Other species sound

    def get_human_years(self):
        """Calculate the pet's age in human years."""
        return self.age * 7  # Convert pet years to human years

def add_pet():
    """Prompt the user to enter pet details and create a Pet object."""
    name = input("Enter pet name: ")  # Get pet name from user
    while True:  # Loop until valid age is entered
        try:
            age = int(input("Enter pet age: "))  # Get pet age and convert to integer
            break  # Exit loop if conversion is successful
        except ValueError:
            print("Invalid age. Please enter a number.")  # Handle invalid input
    species = input("Enter pet species: ")  # Get pet species from user
    return Pet(name, age, species)  # Return a new Pet object

def save_pet_to_file(pet):
    """Save the pet's information to a file."""
    with open("pets.txt", "a") as file:  # Open the file in append mode
        file.write(f"{pet.name},{pet.age},{pet.species}\n")  # Write pet details to the file

def load_pets_from_file():
    """Load pets from a file and return a list of Pet objects."""
    pets = []  # Initialize an empty list to store pets
    try:
        with open("pets.txt", "r") as file:  # Open the file in read mode
            for line in file:  # Read each line in the file
                name, age, species = line.strip().split(',')  # Split line into components
                pets.append(Pet(name, int(age), species))  # Create Pet object and add to list
    except FileNotFoundError:
        print("No pets found. Please add pets first.")  # Handle case where file does not exist
    return pets  # Return the list of Pet objects

def main():
    """Main function to run the pet management system."""
    while True:  # Loop to display the menu
        print("\nMenu:")
        print("1. Add Pet")  # Option to add a pet
        print("2. Save Pet to File")  # Option to save pet to file
        print("3. Load Pets from File")  # Option to load pets from file
        print("4. Exit")  # Option to exit the program
        
        choice = input("Choose an option: ")  # Get user choice
        
        if choice == '1':
            pet = add_pet()  # Add a new pet
            print(f"Added pet: {pet.name}, Age: {pet.age}, Species: {pet.species}")  # Confirm addition
        elif choice == '2':
            if 'pet' in locals():  # Check if a pet has been added
                save_pet_to_file(pet)  # Save the pet to file
                print("Pet information saved to file.")  # Confirm saving
            else:
                print("No pet to save. Please add a pet first.")  # Prompt to add a pet first
        elif choice == '3':
            pets = load_pets_from_file()  # Load pets from file
            if pets:  # Check if any pets were loaded
                print("Loaded Pets:")  # Display loaded pets
                for p in pets:
                    print(f"Name: {p.name}, Age: {p.age}, Species: {p.species}, Age in Human Years: {p.get_human_years()}")  # Show pet details
            else:
                print("No pets found in the file.")  # Inform if no pets were found
        elif choice == '4':
            print("Exiting the program.")  # Confirm exit
            break  # Exit the loop and end the program
        else:
            print("Invalid option. Please try again.")  # Handle invalid menu option

# Call the main function to start the program
main()  # Start the pet management system