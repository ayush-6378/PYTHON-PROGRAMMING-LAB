try:
    # We ask for a number and explicitly convert it to an integer
    val1 = int(input("Enter a number: "))
    
    # We ask for text (a string)
    val2 = input("Enter a text word: ")
    
    # Attempting to add an integer and a string will cause a TypeError
    result = val1 + val2
    print("Result:", result)
    
except TypeError:
    print("Error: You have incompatible data types. You cannot add a number and text together.")
except ValueError:
    print("Error: You didn't enter a valid number for the first value.")