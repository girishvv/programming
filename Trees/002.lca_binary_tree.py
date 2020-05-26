# -*- coding: utf-8 -*-

# Use this class to create binary trees.
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    # Overriding the equality operator.
    # This will be used for testing your solution.
    def __eq__(self, other):
        if type(other) is type(self):
            return self.value == other.value
        return False


# Implement your function below.
def lcaUtil(root, j, k):
    if root is None:
        return None
    if root.value == j or root.value == k:
        return root
    
    lca_left = lcaUtil(root.left,j,k)
    lca_right = lcaUtil(root.right,j,k)
    
    if lca_left and lca_right:
        return root
    
    return lca_left if lca_left else lca_right
    #return None

def lca(root,j,k):
    if not find_node(root,j) or not find_node(root,k):
        return None
    return lcaUtil(root, j, k)

def find_node(root,j):
    if root is None:
        return False
    if root.value == j:
        return True
    return find_node(root.left,j) or find_node(root.right,j)
    #return True
# A function for creating a tree.
# Input:
# - mapping: a node-to-node mapping that shows how the tree should be constructed
# - head_value: the value that will be used for the head ndoe
# Output:
# - The head node of the resulting tree
def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head


# NOTE: The following values will be used for testing your solution.

# The mapping we're going to use for constructing a tree.
# {0: [1, 2]} means that 0's left child is 1, and its right
# child is 2.
mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
head1 = create_tree(mapping1, 0)
# This tree is:
# head1 = 0
#        / \
#       1   2
#      /\   /\
#     3  4 5  6


mapping2 = {5: [1, 4], 1: [3, 8], 4: [9, 2], 3: [6, 7]}
head2 = create_tree(mapping2, 5)
# This tree is:
#  head2 = 5
#        /   \
#       1     4
#      /\    / \
#     3  8  9  2
#    /\
#   6  7


# lca(head1, 1, 5) should return 0
print(lca(head1, 1, 5))
# lca(head1, 3, 1) should return 1
print(lca(head1, 3, 1))
# lca(head1, 1, 4) should return 1
print(lca(head1, 1, 4))
# lca(head1, 0, 5) should return 0
print(lca(head1, 0, 5))
# lca(head2, 4, 7) should return 5
print(lca(head2, 4, 7))
# lca(head2, 3, 3) should return 3
print(lca(head2, 3, 3))
# lca(head2, 8, 7) should return 1
print(lca(head2, 8, 7) )
# lca(head2, 3, 0) should return None (0 does not exist in the tree)
print(lca(head2, 3, 0))

