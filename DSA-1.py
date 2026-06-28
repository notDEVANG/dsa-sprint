# Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target. Each input has exactly one solution, and you can't use the same element twice.
# Example: nums = [2, 7, 11, 15], target = 9 → return [0, 1] (because 2 + 7 = 9).

nums = [2, 7, 11, 15]


for i in nums:
    for j in nums:
        if i + j == 9:
            print(i, j)



nums = [2, 7, 11, 15]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 9:                     #this gives the time complexity of O(n**2)
            print([i, j])

def two_sum(nums, target):
    seen = {}                  # number -> index

    for i in range(len(nums)):
        complement = target - nums[i]         # the number you need (one subtraction)

        if complement in seen: # have I seen it already?
            return [seen[complement], i]           # the two indices
        seen[nums[i]] = i            # store current number so future numbers can find it
print(two_sum([2,7,11,15],9))   # problem guarantees a solution, so no return needed after loop