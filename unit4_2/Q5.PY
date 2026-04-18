while True:
    try:
        num = int(input("Please enter a positive integer: "))
        
        if num < 0:
            print("Error: You entered a negative number. Let's try again.")
        else:
            print("Great job! You entered the valid number:", num)
            break  # Exit the loop because the input was correct
            
    except ValueError:
        # Runs if they type decimals, letters, or symbols
        print("Error: Invalid input. Please make sure you enter a whole number.")