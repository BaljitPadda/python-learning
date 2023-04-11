
""" Thursday 27th January 2022
Task = Create a function that finds the maximum number in a list
"""

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max



# Method 1:

def method_1():
    numbers = [10, 9, 8, 7, 5, 4, 6, 3, 2, 1]
    numbers.sort()
    print(max(numbers))


# Method 2:

def method_2():
    numbers = [10, 9, 8, 7, 5, 4, 6, 3, 2, 1]
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    print(max)


numbers = 3, 4, 5, 6, 100, 600, 225, 50
print(find_max(numbers))






