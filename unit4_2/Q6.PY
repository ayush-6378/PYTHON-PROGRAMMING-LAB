try:
    # Attempting to open a file that does not exist on your computer
    file = open("missing_document.txt", "r")
    
    content = file.read()
    print(content)
    
    file.close()
    
except FileNotFoundError:
    # This block runs instead of crashing the program
    print("Error: The file you are trying to open could not be found.")