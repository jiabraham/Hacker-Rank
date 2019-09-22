""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    BST = []
    distinct = {}
    traverseBST(root, BST)
    for i in range(0, len(BST)-1):
        if BST[i] > BST[i+1]:
            return False
        if BST[i] in distinct:
            return False
        distinct[BST[i]] = 1
    return True

    
    
def traverseBST(root, BST):
    if root.left:
        traverseBST(root.left, BST)
    BST.append(root.data)
    if root.right:
        traverseBST(root.right, BST)
    
