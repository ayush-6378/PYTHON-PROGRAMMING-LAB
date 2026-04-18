# Create three separate dictionaries
dict1 = {1: 'Apple', 2: 'Banana'}
dict2 = {3: 'Cat', 4: 'Dog'}
dict3 = {5: 'Elephant', 6: 'Fox'}

# Create an empty fourth dictionary
dict4 = {}

# Update the empty dictionary with items from the first three
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)

print("Concatenated Dictionary:")
print(dict4)