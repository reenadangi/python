class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root:
            self._insert(self.root,value)
        else:
            self.root=Node(value)
    def _insert(self,cur_node,value):
            if cur_node.value>value:
            # insert in left
                if cur_node.left==None:
                    cur_node.left=Node(value)
                else:
                    self._insert(cur_node.left,value)
            else:
                if cur_node.right==None:
                    cur_node.right=Node(value)
                else:
                    self._insert(cur_node.right,value)
    def printInorder(self):
        if self.root:
            self._printInorder(self.root)
    def _printInorder(self,cur_node):
        if cur_node:
            # First recur on left child 
            self._printInorder(cur_node.left) 
    
            # then print the data of node 
            print(cur_node.value)
    
            # now recur on right child 
            self._printInorder(cur_node.right) 

                
    def height(self):
        if self.root:
            return self._height(self.root)
    def _height(self,cur_node):
        if cur_node==None:
            return -1
        else:
            left_height=self._height(cur_node.left)
            right_height=self._height(cur_node.right)
            return max(left_height,right_height)+1
    def max_element(self):
            # travel right most node 
            if self.root:
                cur_node=self.root
                max=0
                while cur_node:
                    if max<cur_node.value:
                        max=cur_node.value
                    cur_node=cur_node.right
                return max







bst=BST()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(3)
bst.printInorder()
print(bst.height())
print(bst.max_element())

        