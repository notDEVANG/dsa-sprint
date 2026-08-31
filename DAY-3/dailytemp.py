def dailytemp(temp):
    ans = [0] * len(temp)
    stack = []

    for i in range(len(temp)):
        while stack and temp[i] > temp[stack[-1]]:
            prev = stack.pop()
            ans[prev] = i - prev
        stack.append(i)
    return ans
print(dailytemp([73, 74, 75, 71, 69, 72, 76, 73]))