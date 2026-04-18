# Start with an empty queue
queue = []

while True:
    print("\n--- Queue Menu ---")
    print("1. Enqueue (Add element)")
    print("2. Dequeue (Remove element)")
    print("3. Display Queue")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        item = input("Enter the element to add: ")
        queue.append(item) # Adds to the end of the list
        print(item, "was added to the queue.")
        
    elif choice == '2':
        if len(queue) == 0:
            print("Queue is empty! Nothing to dequeue.")
        else:
            # pop(0) removes and returns the first element in the list
            removed_item = queue.pop(0) 
            print(removed_item, "was removed from the queue.")
            
    elif choice == '3':
        print("Current Queue status:", queue)
        
    elif choice == '4':
        print("Exiting program...")
        break # Stops the infinite while loop
        
    else:
        print("Invalid choice! Please try again.")