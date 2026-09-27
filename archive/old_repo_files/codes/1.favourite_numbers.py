# Concepts
# 1. Falsy and Truthy values
# 2. Infinite loops with break condition
# 3. Sanitizing inputs with .strip()

# Create an empty dictionary to store favorite numbers
fav_numbers = {}

# Infinite loop for input
while True:
    name = input("What's your first name? ").strip()
    input("Press Enter to continue...")
    
    number = input("What's your favorite number: ").strip()
    input("Press Enter to continue...")
    
    # Store the name-number pair in the dictionary
    fav_numbers[name] = number
    print("\nCurrent favorites:", fav_numbers)

    # Ask the user whether to stop or continue
    stop_cmd = input("Type NO[N] then Enter to exit or any key to continue: ").strip()
    
    # Check if user wants to break the loop
    if stop_cmd.upper() in ["NO", "N"]:
        break
    else:
        print("Continuing...\n")

# Display final results
print("\nFavorite numbers:")
for name, number in fav_numbers.items():
    print(f"{name}'s favorite number is {number}")
