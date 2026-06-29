# Two Sum II — Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers that add up to a target. 
# Return their indices [index1, index2] (1-indexed, and index1 < index2). 
# Exactly one solution exists; you can't reuse an element.
# Example: numbers = [2, 7, 11, 15], target = 9 → [1, 2] (because 2 + 7 = 9, at 1-indexed positions 1 and 2).

def two_sum(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left < right:

        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

print(two_sum(numbers = [2,7,11,15],target = 9))