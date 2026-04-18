import random

# Generate 30 random numbers
all_numbers = []
for i in range(30):
    all_numbers.append(random.randint(-50, 50))
    
print("Original Mixed List:")
print(all_numbers)

# Create two empty lists
positive_list = []
negative_list = []

# Sort them into their respective lists
for num in all_numbers:
    if num > 0:
        positive_list.append(num)
    elif num < 0:
        negative_list.append(num)
        # Note: We ignore 0 as it is neither positive nor negative

print("\nList of Positive Numbers:")
print(positive_list)

print("\nList of Negative Numbers:")
print(negative_list)