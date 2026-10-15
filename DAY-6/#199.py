import collections

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

def rightSideView(self, root):
        res = []

        q = collections.deque([root])

        while q:
            rightSide = None
            qlen = len(q)

            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res

#dfs

# def dfs(node, depth):
#     if not node:
#         return
    
#     # If we reach a level we haven't added to our result yet
#     if depth == len(res):
#         res.append(node.val)
    
#     # Traverse right first, then left
#     dfs(node.right, depth + 1)
#     dfs(node.left, depth + 1)

# dfs(root, 0)
# return res