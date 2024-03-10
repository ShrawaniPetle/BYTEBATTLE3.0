def find_middle(lst):
    length = len(lst)
    if length % 2 == 0:
        middle_index = length // 2
        return lst[middle_index - 1], lst[middle_index]
    else:
        middle_index = length // 2
        return lst[middle_index]

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Middle element(s) of the list:", find_middle(my_list))

