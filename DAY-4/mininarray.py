def findmin(nums):
    l, r = nums[0], len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[r] < nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return nums[l]

print(findmin([3,4,5,1,2]))