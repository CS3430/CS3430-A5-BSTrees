from BSTNode import BSTNode

## bugs to vladimir dot kulyukin at usu dot edu

class BSTree:

    def __init__(self, root=None):
        self.__root = root
        if root==None:
            self.__numNodes = 0
        else:
            self.__numNodes = 1

    def getRoot(self):
        return self.__root

    def getNumNodes(self):
        return self.__numNodes

    def isEmpty(self):
        return self.__root == None

    def hasKey(self, key):
        if self.isEmpty():
            return False;
        currNode = self.__root
        while currNode != None:
            if key == currNode.getKey():
                return True
            if key < currNode.getKey():
                currNode = currNode.getLeftChild()
            elif key > currNode.getKey():
                currNode = currNode.getRightChild()
        return False

    def insertKey(self, key):
        if self.isEmpty():
            self.__root = BSTNode(key=key)
            self.__numNodes += 1
            return True
        elif self.hasKey(key):
            return False
        else:
            currNode = self.__root
            parNode = None
            while currNode != None:
                parNode = currNode
                if key < currNode.getKey():
                    currNode = currNode.getLeftChild()
                elif key > currNode.getKey():
                    currNode = currNode.getRightChild()
                else:
                    raise Exception('insertKey: ' + str(key))
            if parNode != None:
                if key < parNode.getKey():
                    parNode.setLeftChild(BSTNode(key=key))
                    self.__numNodes += 1
                    return True
                elif key > parNode.getKey():
                    parNode.setRightChild(BSTNode(key=key))
                    self.__numNodes += 1
                    return True
                else:
                    raise Exception('insertKey: ' + str(key))
            else:
                raise Exception('insertKey: parNode=None; key= ' + str(key))

    def __heightOf(self, node):
        if self.isEmpty():
            return 0
        if node == None:
            return -1;
        return max( self.__heightOf(node.getLeftChild()), self.__heightOf(node.getRightChild()) ) + 1
        
    def heightOf(self):
        return self.__heightOf(self.__root)

    def __isBalanced(self, node):
        if node == None:
            return True
        if abs(self.__heightOf(node.getRightChild()) - self.__heightOf(node.getLeftChild())) > 1:
            return False
        return self.__isBalanced(node.getRightChild()) and self.__isBalanced(node.getRightChild())

    def isBalanced(self):
        if self.isEmpty():
            return True
        return self.__isBalanced(self.__root)

    def __displayInOrder(self, currnode):
        if currnode == None:
            print('NULL')
        else:
            self.__displayInOrder(currnode.getLeftChild())
            print(str(currnode))
            self.__displayInOrder(currnode.getRightChild())

    def displayInOrder(self):
        self.__displayInOrder(self.__root)

    def isList(self):
        return self.__numNodes == self.heightOf() + 1

                


    
            

    
   
