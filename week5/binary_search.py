def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1

    return -1 

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(binary_search(my_list, 30))
print(binary_search(my_list, 60))
print(binary_search(my_list, 110))
