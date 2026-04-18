my_list = [10, 20, 30, 40, 50]

try:
    # Ask the user for an index
    index = int(input("Enter an index between 0 and 4: "))
    
    # Try to access the element at that index
    print("The element at index", index, "is:", my_list[index])
    
except IndexError:
    # This block runs if the index is too high or too low
    print("Error: That index is out of range! Please enter a number from 0 to 4.")
except ValueError:
    # This block runs if the user types letters instead of a number
    print("Error: Please enter a valid whole number.")