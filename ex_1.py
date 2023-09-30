def get_unique_list(input_list):
    unique_elements = []
    seen = set()

    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_elements.append(item)

    return unique_elements

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)
