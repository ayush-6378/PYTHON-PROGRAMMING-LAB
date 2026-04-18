text = input("Enter a string: ")

# Create an empty dictionary to store the character counts
frequency_dict = {}

# Go through each character in the string one by one
for char in text:
    # If character is already in dictionary, increase its count by 1
    if char in frequency_dict:
        frequency_dict[char] = frequency_dict[char] + 1
    # If it is a new character, add it to dictionary with count 1
    else:
        frequency_dict[char] = 1

print("Character Frequencies:")
print(frequency_dict)