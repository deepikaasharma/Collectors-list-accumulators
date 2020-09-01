num_list = [2, 12, 12, 1, 24, 10, 19, 17, 8, 8, 25, 14, 12, 4, 23, 14, 18, 13, 0, 15, 22, 8, 5, 12, 6]

altered_num_list = []
for num in num_list:
    if num % 2 == 0:
        altered_num_list.append(num**2)
    else:
        altered_num_list.append(num**3)


"""What if we want to accumulate the squares and cubes into their own lists? Let's modify the code above:
"""
num_list = [2, 12, 12, 1, 24, 10, 19, 17, 8, 8, 25, 14, 12, 4, 23, 14, 18, 13, 0, 15, 22, 8, 5, 12, 6]

squares = []
cubes = []
for num in num_list:
    if num % 2 == 0:
        squares.append(num**2)
    else:
        cubes.append(num**3)



# following is filtering 
num_list = [2, 12, 12, 1, 24, 10, 19, 17, 8, 8, 25, 14, 12, 4, 23, 14, 18, 13, 0, 15, 22, 8, 5, 12, 6]

divisible_by_3 = []
for num in num_list:
    if num % 3 == 0:
        divisible_by_3.append(num)


# Flattening nested lists

mixed_list = ['word', [1, 2, 3, 4, 5], 43, 90.0]
flattened = []

for item in mixed_list:
    if isinstance(item, list):
        for nested_item in item:
            flattened.append(nested_item)
    else:
        flattened.append(item)


print(flattened)