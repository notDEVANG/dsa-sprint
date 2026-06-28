#Top K Frequent Elements — return the k most frequent numbers in an array. nums = [1,1,1,2,2,3], k = 2 → [1,2].
#  Hint: Counter gets you the frequencies fast. 
# Then you need the top k — think about sorting by count, or for bonus credit, 
# a heap (which you'll formally learn Week 3, but Counter has a .most_common() method worth discovering).

from collections import Counter

def top_k(nums, k):

    count = Counter(nums)

    answer = []

    for num, freq in count.most_common(k):
        answer.append(num)

    return answer

nums = [1,1,1,2,2,3]

print(top_k(nums,2))