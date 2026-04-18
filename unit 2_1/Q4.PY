def reverse_list(lst):
    # Base case: an empty list is just an empty list
    if len(lst) == 0:
        return []
    else:
        # Recursive step: reverse the rest of the list, then add the first item at the end
        return reverse_list(lst[1:]) + [lst[0]]

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Reversed list:", reverse_list(my_list))