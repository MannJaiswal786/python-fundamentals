def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print("Found at index:", x)
            return x
    print("Target is not in the list")
    return -1

my_list = [1,4,6,7,10,15]
linear_search(my_list, 10)
linear_search(my_list, 4)
linear_search(my_list, 2)