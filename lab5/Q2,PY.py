import random

# Generate 20 random integers and store them in a list
num_list = []
for i in range(20):
    num_list.append(random.randint(1, 10))
    
print("Generated List:", num_list)

# Accept a number from the user
search_num = int(input("Enter a number to search for: "))

# Print positions of all occurrences
print("Positions where", search_num, "was found:")
found = False

# We use range(len()) so we can get the index (position)
for i in range(len(num_list)):
    if num_list[i] == search_num:
        print("Index:", i)
        found = True

if found == False:
    print("Number not found in the list.")