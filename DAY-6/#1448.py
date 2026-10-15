# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

def good(root):
    def dfs(node, maxval):
        if not node:
            return 0

        res = 1 if node.val >= maxval else 0
        maxval = max(maxval, node.val)
        res += dfs(node.left, maxval)
        res += dfs(node.right, maxval)
        return res
    dfs(root, root)