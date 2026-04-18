def sanitize_list(lst):
    # Base case: empty list
    if len(lst) == 0:
        return []
    
    first_item = lst[0]
    # Check if we need to replace it
    if first_item < 0:
        first_item = 0
        
    # Recursive step: keep the first item, sanitize the rest
    return [first_item] + sanitize_list(lst[1:])

# Example usage:
mixed_list = [5, -2, 9, -8, 3]
print("Sanitized list:", sanitize_list(mixed_list))