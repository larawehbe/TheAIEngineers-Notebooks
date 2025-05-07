# Function to get a positive integer from the user
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("That's not a valid integer. Please enter a valid positive integer.")

# Ask the user for a positive integer
n1 = get_positive_integer("Enter a valid positive integer: ")
# Check if the number is a multiple of 4
if n1 % 4 == 0:
    print(f"The number {n1} is a multiple of 4.")
# Check if the number is even or odd
if n1 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Ask the user for 2 positive integer numbers and check if the first number can be evenly divided by the second
num = get_positive_integer("Enter the first positive integer: ")
check = get_positive_integer("Enter the second positive integer: ")
if num % check == 0:
    print(f"The number {num} can be evenly divided by {check}.")
else:
    print(f"The number {num} cannot be evenly divided by {check}.")
