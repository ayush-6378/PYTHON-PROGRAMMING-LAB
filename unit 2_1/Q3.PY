def count_vowels(s):
    # Base case: an empty string has 0 vowels
    if s == "":
        return 0
    
    # Check if the very first character is a vowel
    first_char = s[0].lower()
    if first_char in "aeiou":
        # Recursive step: 1 + check the rest of the string
        return 1 + count_vowels(s[1:])
    else:
        # Recursive step: 0 + check the rest of the string
        return 0 + count_vowels(s[1:])

# Example usage:
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))