# Valid Anagram — given two strings s and t, return True if t is an anagram of s (same letters, same counts, reordered). Example: "anagram", "nagaram" → True. Hint: think about what you'd count, and which hash structure counts things. Python's collections.Counter is worth discovering here.

from collections import Counter

def anagram(s,t):
    return Counter(s) == Counter(t)

s = ("apple")
t = ("paple")

result = anagram(s,t)
print(result)


# given a list of strings, group the ones that are anagrams of each other. Example: ["eat","tea","tan","ate","nat","bat"] → [["eat","tea","ate"],["tan","nat"],["bat"]]. Harder. Hint: what could you compute from each word that's identical for all its anagrams — a "signature" you could use as a dict key?

def grp_anagram(words):

    groups = {

    }

    for word in words:
        signature = tuple(sorted(word))

        if signature not in groups:
            groups[signature] = []
        
        groups[signature].append(word)

    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(grp_anagram(words))

#more optimised code

from collections import defaultdict
groups = defaultdict(list)
for word in words:
    groups[tuple(sorted(word))].append(word)
return list(groups.values())


#dict version
def anagram(s, t):

    count_s = {}
    count_t = {}

    for ch in s:
        if ch in count_s:
            count_s[ch] += 1
        else:
            count_s[ch] = 1

    for ch in t:
        if ch in count_t:
            count_t[ch] += 1
        else:
            count_t[ch] = 1

    return count_s == count_t