text = "Python"

print("--- Forward Order ---")
i = 0
while i < len(text):
    print(text[i])
    i += 1

print("\n--- Reverse Order ---")
# Start at the last index (length - 1) and go down to 0
j = len(text) - 1
while j >= 0:
    print(text[j])
    j -= 1