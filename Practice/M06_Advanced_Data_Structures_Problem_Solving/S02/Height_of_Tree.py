class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Tree Structure
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def Height(root):
    if root is None:
        return -1
    l = Height(root.left)
    r = Height(root.right)
    return 1 + max(l, r)

def is_Balanced(root):
    if root is None:
        return True
    l = Height(root.left)
    r = Height(root.right)
    if abs(l - r) <= 1 and is_Balanced(root.left) and is_Balanced(root.right):
        return True
    return False
print(is_Balanced(root))

#LeetCode - 100 Same Tree
class Solution:

  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
      return True

    if not p or not q or p.val != q.val:
      return False

    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#LeetCode - 101 Symmetric Tree
class Solution:

  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
      return True

    def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
      if not t1 and not t2:
        return True
      if not t1 or not t2 or t1.val != t2.val:
        return False
      return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

    return isMirror(root.left, root.right)