# Accept string from the user
user_string = input("Enter a string: ")

vowel_count = 0
vowels = "aeiouAEIOU"

# Go through each character one by one
for char in user_string:
    if char in vowels:
        vowel_count = vowel_count + 1

print("Total vowels:", vowel_count)