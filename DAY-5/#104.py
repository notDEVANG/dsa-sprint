# BFS
# from collections import deque


# def maxDepth(self, root):
#     if not root:
#         return None

#     level = 0
#     q = deque([root])

#     while q:
#         for i in range(len(q)):
#             node = q.popleft()
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         level += 1
#     return level

# DFS

def maxDepth(self, root):
    if not root:
        return None

    stack = [[root, 1]]
    res = 1

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res