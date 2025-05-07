def finalList(check):
    permanent = []
    # If list length is 2 or less, return the list itself
    if len(check) <= 2:
        permanent = check
        return permanent
    else:
        # Return a new list containing only the first and last elements
        permanent = [check[0], check[-1]]
        return permanent

newList = []

print("Enter numbers to add to list. Press Enter without input to finish.")

while True:
    user_input = input("Enter a number (or press Enter to finish): ")
    if user_input == '':
        # User chose to finish input
        break
    try:
        num = int(user_input)
        newList.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print(f"the original list {newList}")
print(f"the final editted list {finalList(newList)}")
