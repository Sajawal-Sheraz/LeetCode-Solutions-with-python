class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p = TreeNode(val=1)
p.left = TreeNode(val=2)
p.right = TreeNode(val=3)

q = TreeNode(val=1)
q.left = TreeNode(val=2)
q.right = TreeNode(val=3)


# Solution
def isSameTree(p, q) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    left_same = isSameTree(p.left, q.left)
    right_same = isSameTree(p.right, q.right)
    return left_same and right_same


print(isSameTree(p, q))
