# Valid Palindrome

# Given a string s, return True if it's a palindrome, considering only alphanumeric characters and ignoring case. 
# Empty string counts as a palindrome.
# Example: "A man, a plan, a canal: Panama" → True (ignoring spaces/punctuation/case, it reads the same forwards and backwards). 
# "race a car" → False.

# way 1st: cleaned string

def is_palindorme(s):

    cleaned = ""

    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()

    return cleaned == cleaned[::-1]

print(is_palindorme("A man, a plan, a canal: Panama"))
print(is_palindorme("hello hello"))

# way 2nd:two-pointers

def is_palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("0P"))            