#Product of Array Except Self
#return an array where each position holds the product of all other elements, and you can't use division.
#[1,2,3,4] → [24,12,8,4]. This one's a genuine step up and breaks the hashing pattern — it's about prefix/suffix products.
#Struggle with it for 20 min; if it won't crack, bring me your partial thinking and we'll work it together.
#It's okay if this one beats you solo — it beats most people.

def product_except_self(nums):
    n = len(nums)

    # Create arrays
    prefix = [1] * n
    suffix = [1] * n
    answer = [1] * n

    # Build prefix array
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Build suffix array
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Multiply prefix and suffix
    for i in range(n):
        answer[i] = prefix[i] * suffix[i]

    return answer


nums = [1, 2, 3, 4]

print(product_except_self(nums))

#optimized(only two variables)

def product_except_self(nums):
    n = len(nums)

    answer = [1] * n

    # Build prefix products directly into answer
    prefix = 1

    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Multiply by suffix products
    suffix = 1

    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


nums = [1,2,3,4]

print(product_except_self(nums))