# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/30/2022
# Description: Write a function that takes as a parameter a list of numbers. The function
# should return the statistical median of those numbers, which will require it to sort the list.

def find_median(numbers):
    """ Finds the median number in any list of numbers."""
    numbers.sort()
    if len(numbers) % 2 == 1:
        return numbers[len(numbers) // 2]
    else:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2

# print(find_median([13, 7, -3, 82, 4]))
# print(find_median([7, 82, 4, -7, 13]))
# print(find_median([64, 75, 2, -13, 189]))
