#conner martinez
#11/9/2021
#css 225
#problem 4:a list of numbers and returns a new list with unique elements of the first list
def unique_list(numbers):
    unique = []
    for item in numbers :
        if item not in unique:
            unique.append(item)
    return unique

print(unique_list([1, 3, 3, 3, 6, 2, 3, 5]))
# [1, 2, 3]