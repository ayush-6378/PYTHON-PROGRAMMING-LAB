user_string = input("Enter a string: ")

if len(user_string) > 0:
    print("First character:", user_string[0])
    print("Last character:", user_string[-1])
    
    # Check if the length is an odd number
    if len(user_string) % 2 != 0:
        # Use integer division // to find the exact middle index
        middle_index = len(user_string) // 2
        print("Middle character:", user_string[middle_index])
else:
    print("You entered an empty string.")