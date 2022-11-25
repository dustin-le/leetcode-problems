# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # My solution
    # pathToP, pathToQ = [], []
    
    # temp = root
    
    # while temp != None:
    #     pathToP.append(temp)
    #     if (temp.val > p.val):
    #         temp = temp.left
    #     elif (temp.val < p.val):
    #         temp = temp.right
    #     else:
    #         temp = root
    #         break
            
    # while temp != None:
    #     pathToQ.append(temp)
    #     if (temp.val > q.val):
    #         temp = temp.left
    #     elif (temp.val < q.val):
    #         temp = temp.right
    #     else:
    #         break
            
    # for i in range(min(len(pathToP), len(pathToQ))):
    #     if pathToP[i] == pathToQ[i]:
    #         continue
    #     else:
    #         return pathToP[i-1]
    
    # if (len(pathToP) < len(pathToQ)):
    #     return pathToP[-1]
    # return pathToQ[-1]
    
    while root != None:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
            
root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = TreeNode(0)
q = TreeNode(5)

print(lowestCommonAncestor(root, p, q).val)