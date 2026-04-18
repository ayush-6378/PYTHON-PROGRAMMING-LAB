import random

# Generate 50 random numbers in the range 1 to 30
numbers = []
for i in range(50):
    numbers.append(random.randint(1, 30))
    
print("Original List with 50 numbers:")
print(numbers)

# Remove duplicates
unique_numbers = []
for num in numbers:
    # Only append if the number is not already in our new list
    if num not in unique_numbers:
        unique_numbers.append(num)

print("\nList after removing duplicates:")
print(unique_numbers)