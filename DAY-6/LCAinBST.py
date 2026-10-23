def lca(self, root, p, q):
    curr = root

    while curr:
        if p.val > curr.val