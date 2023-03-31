from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def dfs(root, counter=0):
#     global maxCounter
#     if root:
#         counter += 1
#         dfs(root.left, counter)
        
#         maxCounter = max(maxCounter, counter)
        
#         dfs(root.right, counter)
    
#     return maxCounter
        
        
def isBalanced(root):
    Bal = True
    
    def dfs(node):
        if not node: return 0
        lft = dfs(node.left) 
        rgh = dfs(node.right)
        if abs(lft - rgh) > 1: Bal = False
        return max(lft, rgh) + 1
        
    dfs(root)
    return Bal

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(isBalanced(root))

# def isBalanced(root: 'TreeNode') -> bool:
    
#     if not root:
#         return True
    
#     left = dfs(root.left)
#     global maxCounter
#     maxCounter = 0
#     right = dfs(root.right)
    
#     return (abs(left - right)) <= 1