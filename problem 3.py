#conner martinez
#11/9/2021
#css 225
#problem 3: multiplys all the numbers in the list


#problem 3
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((5, 2, 7, -1,)))