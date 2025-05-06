def linear_search_dictionary(dictionary, target):
    for key, value in dictionary.items():
        if value == target:
            print(f"Found ${target} at ${key}")
            return key
        
        
    print(f"${target} not found or doesnt exist")
    return None
        
my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
