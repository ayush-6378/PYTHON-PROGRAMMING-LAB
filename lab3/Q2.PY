def to_lower(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32) # Add 32 to make it lowercase
        else:
            result += char
    return result

def to_upper(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32) # Subtract 32 to make it uppercase
        else:
            result += char
    return result

def to_toggle(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

# Testing the functions
my_string = "PyThOn 123!"
print("Original:", my_string)
print("Lower:", to_lower(my_string))
print("Upper:", to_upper(my_string))
print("Toggle:", to_toggle(my_string))