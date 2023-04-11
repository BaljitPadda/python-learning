"""
Sunday 9th January 2022
Task: Removing duplicates from a list of numbers
"""

numbers = [1, 1, 7, 8, 3, 5, 7, 9, 8, 1]
numbers.sort()
print(numbers)
for item in numbers:
    if numbers.count(item) > 1:
        numbers.remove(item)
print(numbers)

numbers = [1, 1, 7, 8, 3, 5, 7, 9, 8, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        uniques.sort()
print(uniques)