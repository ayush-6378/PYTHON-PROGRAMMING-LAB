try:
    marks = float(input("Enter the student's marks (0 to 100): "))
    
    # Check if marks are logically incorrect
    if marks < 0 or marks > 100:
        # Manually trigger an error with a custom message
        raise ValueError("Invalid entry. Marks must be between 0 and 100.")
        
    print("Marks successfully recorded:", marks)
    
except ValueError as error_message:
    # This will print either the custom message above, or a standard error if they typed text
    print("Error:", error_message)