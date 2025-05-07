newList = []
def checkList(prompt):
    print(f"the sorted list: {newList}")
    for i in range(len(newList)):
        if newList[i]== prompt:
            print(f"The number {prompt} is in the list.")
            return True
    print(f"the number {prompt} is not in the list.")
    return False

print ("Enter numbers to append to the list (or press enter without a number to stop):")
while True:
    user_input = input("Enter a number or press enter to stop: ")
    if user_input == '':
        break
    else:
        try:
            num = int(user_input)
            newList.append(num)
            newList.sort()
        except ValueError:
            print("Invalid input. Please enter a number or press enter to stop.")

while True:
    user_input_check = input("Enter a valid integer to check if it is in the list (or press enter to skip): ")
    if user_input_check == '':
        print("you have exited the program without entering a valid number.")
        break
    else:
            try:
                x = int(user_input_check)
                checkList(x)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
