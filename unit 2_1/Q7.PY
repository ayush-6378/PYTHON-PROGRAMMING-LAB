# Helper recursive function to get the total sum
def get_sum(lst):
    # Base case: sum of an empty list is 0
    if len(lst) == 0:
        return 0
    else:
        # Recursive step: first item + sum of the rest of the list
        return lst[0] + get_sum(lst[1:])

def get_average(lst):
    # Prevent crashing if the list is empty
    if len(lst) == 0:
        return 0
    
    total = get_sum(lst)
    average = total / len(lst)
    return average

# Example usage:
number_list = [10, 20, 30, 40]
print("Average of the list:", get_average(number_list))