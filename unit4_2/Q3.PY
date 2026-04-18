total_sum = 0

try:
    print("Keep entering numbers to add. Press Ctrl+C to stop.")
    while True:
        # Get a number from the user
        num = float(input("Enter a number: "))
        total_sum = total_sum + num
        
except KeyboardInterrupt:
    # This runs when the user presses Ctrl+C
    print("\nProgram stopped gracefully by the user.")
    print("The total sum of the numbers you entered is:", total_sum)