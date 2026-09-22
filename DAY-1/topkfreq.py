def k_top(nums, k):
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    buckets = [[] for _ in range(len(nums) - 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []

    for freq in range(len(buckets)):
        for num in buckets[freq]:
            result.append(num)

            if len(result) == k:
                return result