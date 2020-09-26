num_list = [4,5,6,7,3,1,76,2,4]
#num_list = [4,5]
class Node:
    data = None
    left = None
    right = None
    def __init__(self,num):
        self.data = num

def insertTree(node, x):
    if node==None:
        return Node(x)
    if(x <= node.data):
        print(x)
        node.left = insertTree(node.left,x)
    else:
        print("check ",x)
        node.right = insertTree(node.right,x)
    return node
def create_t(num_list):
    node = None
    for x in num_list:
        node = insertTree(node,x)
    return node

node  = create_t(num_list)

'''traverse thr tree'''
def traverse_t(node):
    if(node==None):
        return
    print(node.data)
    if(not node.left == None):
        traverse_t(node.left)
    if(not node.right == None):
        traverse_t(node.right)

traverse_t(node)
