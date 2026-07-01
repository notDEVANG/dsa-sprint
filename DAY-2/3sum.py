# Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that i, j, k 
# are different indices and nums[i] + nums[j] + nums[k] == 0.
# No duplicate triplets in the output.
# Example: nums = [-1, 0, 1, 2, -1, -4] → [[-1, -1, 2], [-1, 0, 1]].

def three_sum(nums):

    nums.sort()

    result = []

    for i in range(len(nums)-2):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = len(nums)-1

        while left < right:

            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1

            elif total > 0:
                right -= 1

            else:

                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1

                while left < right and nums[right] == nums[right+1]:
                    right -= 1

    return result


nums = [-1,0,1,2,-1,-4]

print(three_sum(nums))