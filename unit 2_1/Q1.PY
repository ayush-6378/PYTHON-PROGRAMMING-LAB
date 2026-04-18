def prime_factors(n, divisor=2):
    # Base case: if the number becomes 1, we are done
    if n <= 1:
        return
    
    # If the number is divisible by our current divisor, print it
    if n % divisor == 0:
        print(divisor, end=", ")
        # Recursive step: divide the number and call the function again
        prime_factors(n // divisor, divisor)
    else:
        # Recursive step: if not divisible, try the next divisor (divisor + 1)
        prime_factors(n, divisor + 1)

# Example usage:
num = int(input("Enter a positive integer: "))
print("Prime factors:")
prime_factors(num)