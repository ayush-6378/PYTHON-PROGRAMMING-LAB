# A list containing 5 strings
words = ["python", "java", "c++", "ruby", "javascript"]
print("Original strings:", words)

# Create a new list to hold the uppercase versions
upper_words = []

for word in words:
    upper_words.append(word.upper())

print("Uppercase strings:", upper_words)