user_string = input("Enter a string: ")

total_length = len(user_string)
vowels_count = 0
consonants_count = 0
vowels_list = "aeiouAEIOU"

for char in user_string:
    # Check if the character is a letter
    if char.isalpha():
        if char in vowels_list:
            vowels_count += 1
        else:
            consonants_count += 1

print("Total length:", total_length)
print("Count of vowels:", vowels_count)
print("Count of consonants:", consonants_count)