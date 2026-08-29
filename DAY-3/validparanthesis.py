def validpara(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
        }

    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                