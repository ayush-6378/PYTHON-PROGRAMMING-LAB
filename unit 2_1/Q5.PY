def calculate_power(a, b):
    # Base case: anything to the power of 0 is 1
    if b == 0:
        return 1
    else:
        # Recursive step: multiply 'a' by the power of 'a' to the (b-1)
        return a * calculate_power(a, b - 1)

# Example usage:
base = int(input("Enter base (a): "))
power = int(input("Enter power (b): "))
print(f"{base} raised to {power} is:", calculate_power(base, power))