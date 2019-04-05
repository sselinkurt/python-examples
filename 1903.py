#binary search tree

class myNode(object):
    def __init__(self, v=0): #value ya bir sey gondermezsen 0 al 
        self.value = v
        self.left = None
        self.right = None

class myTree(object):
    def __init__(self):
            self.root = myNode(250)

    def insert(self, node_1):
        if(self.root.value>node_1.value):
            self.root.left = node_1
        elif(self.root.value<node_1.value):
            self.root.right = node_1
        else:
            print("duplicate error")

##butun agaci print eden fonksiyon            
def printTree(tree_1):
    while(tree_1.left!=None):
        printTree(tree_1.left)
    print(tree_1.value)
    while(tree_1.right!=None):
        printTree(tree_1.right)

def test():
    T1 = myTree() #root 250
    T1.insert(myNode(-20))
    T1.insert(myNode(300))
    print(T1.root.left.value)
    print(T1.root.value)
    print(T1.root.right.value)
test()


