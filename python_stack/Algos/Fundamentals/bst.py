class Node:
    def __init__(self,value=None):
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
            # push it to the left
            if cur_node.left==None:
                cur_node.left=Node(value)
            else:
                self._insert(cur_node.left,value)
        else:
            # push it to the right
            if cur_node.right==None:
                cur_node.right=Node(value)
            else:
                self._insert(cur_node.right,value)
    def printTree(self):
        if self.root:
            self._printTree(self.root)
    def _printTree(self,cur_node):
        if cur_node:
            self._printTree(cur_node.left)
            print(cur_node.value)
            self._printTree(cur_node.right)
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
    def contains(self,value):
        if self.root:
            return self._contains(self.root,value)
    def _contains(self,cur_node,value):
        if cur_node==None:
            return False
        if cur_node.value==value:
            return True
        if cur_node.value>value:
            return self._contains(cur_node.left,value)
        else:
            return self._contains(cur_node.right,value)
    def max(self):
        if self.root:
            cur_node=self.root
            max=0
            while cur_node:
                max=cur_node.value
                cur_node=cur_node.right
            return max
    def min(self):
        if self.root:
            cur_node=self.root
            min=0
            while cur_node:
                min=cur_node.value
                cur_node=cur_node.left
            return min
    def delete(self,value):
        if self.root:
            self._delete(self.root,value)
    def _delete(self,cur_node,value):
        # node to be deleted has no child
        #node to be deleted has only one child
        # node to be delete has two children
        if cur_node==None:
            return cur_node

        if value<cur_node.value:
            # it is in left sub tree
            cur_node.left=self._delete(cur_node.left,value)
            
        elif value>cur_node.value:
            cur_node.right=self._delete(cur_node.right,value)
            return cur_node
        else:
            # this node to be deleted
            # if no child
            if cur_node.left==None and cur_node.right==None:
                return None
            # if one child
            if cur_node.left==None:
                return cur_node.right
            if cur_node.right==None:
                return cur_node.left
            # if two children
            prev=cur_node.left
            while prev.right:
                prev=prev.right
            self._delete(cur_node,prev.value)
            prev.right=cur_node.right
            prev.left=cur_node.left
            return prev








bst=BST()
bst.insert(12)
bst.insert(14)
bst.insert(10)
bst.insert(8)
bst.insert(27)
bst.delete(10)
bst.printTree()
print(f"Height {bst.height()}")
print(f"Contains: {bst.contains(12)}")
print(f"Maximum value:{bst.max()}")
print(f"Minimum value:{bst.min()}")
