# Given an integer array nums, return True if any value appears at least twice, and False if every element is distinct.
# Example: [1, 2, 3, 1] → True (the 1 repeats). [1, 2, 3, 4] → False.

def duplicates(nums):


    
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False

nums = [1,2,3,1]
print(duplicates(nums))