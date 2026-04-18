def get_binary(n):
    # Base cases: binary of 0 is "0", binary of 1 is "1"
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        # Recursive step: get the binary of the division by 2, and add the remainder
        return get_binary(n // 2) + str(n % 2)

# Example usage:
num = int(input("Enter a positive integer: "))
print("Binary equivalent:", get_binary(num))