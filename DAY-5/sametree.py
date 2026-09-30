def sametree(self, p, q):
    if not p and not q:
        return True 
    if not p or not q or not p.val != q.val:
        return False

    return (
        self.sametree(p.left, q.left) and
        self.sametree(p.right, q.right)
    )