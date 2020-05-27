#Given a binary tree, we need to count the number of unival subtrees 
#(all nodes have same value).
# O(n)
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def count_unival_trees(root):
    if root is None:
        return 0
    count = [0]
    
    count_unival_trees_util(root,count)
    return count[0]
def count_unival_trees_util(root,count):
    if root is None:
        return True
    
    left = count_unival_trees_util(root.left,count)
    right = count_unival_trees_util(root.right,count)
    
    if left == False or right == False:
        return False
    if root.left and root.data != root.left.data:
        return False
    if root.right and root.data !=root.right.data:
        return False
    
    count[0] +=1
    
    return True
if __name__ == "__main__":
    root = Node(5) 
    root.left = Node(4) 
    root.right = Node(5) 
    root.left.left = Node(4) 
    root.left.right = Node(4) 
    root.right.right = Node(4)
    
    print(count_unival_trees(root))