from isBalanced import isBalanced, TreeNode

def test1():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert isBalanced(root) == True

def test2():
    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8)), TreeNode(5)), TreeNode(3, TreeNode(6)))
    assert isBalanced(root) == True

def test3():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    assert isBalanced(root) == False

def test4(): 
    root = TreeNode(1, TreeNode(2))
    assert isBalanced(root) == True
    
def test5():
    root = []
    assert isBalanced(root) == True
    
def test6():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert isBalanced(root) == False
    
def test7():
    

