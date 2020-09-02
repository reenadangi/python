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
        return self
    def _insert(self,cur_node,value):
        if cur_node.value>value:
            if cur_node.left:
                self._insert(cur_node.left,value)
            else:
                cur_node.left=Node(value)
        else:
            if cur_node.right:
                self._insert(cur_node.right,value)
            else:
                cur_node.right=Node(value)

    def display(self):
        print(self.root.value)
        if self.root:
            self._display(self.root)
    def _display(self,cur_node):
        if cur_node:
            self._display(cur_node.left)
            print(cur_node.value)
            self._display(cur_node.right)
    # A utility function to search a given key in BST 

    def search(self,n):
        if self.root:
            return self._search(self.root,n)
    def _search(self,cur_node,n):
       # Base condition
        if cur_node is None or cur_node.value==n:
            return cur_node
        if cur_node.value>n:
            return self._search(cur_node.left,n) 
        else:
            return self._search(cur_node.right,n)
    def contains(self,value):
        if self.root:
            return self._containts(self.root,value)
    def _containts(self,cur_node,value):
        if cur_node is None:
            return False
        if cur_node.value==value:
            return True
        if cur_node.value>value:
            return self._containts(cur_node.left,value)
        else:
            return self._containts(cur_node.right,value)
    def max(self):
        if self.root:
            cur_node=self.root
            max_value=cur_node.value
            while cur_node:
                if cur_node.value>max_value:
                    max_value=cur_node.value
                cur_node=cur_node.right
        return max_value
    def min(self):
        if self.root:
            cur_node=self.root
            min_value=cur_node.value
            while cur_node:
                if cur_node.value<min_value:
                    min_value=cur_node.value
                cur_node=cur_node.left
        return min_value                
    def height(self):
        if self.root:
           return self._height(self.root)
    def _height(self,cur_node):
        if cur_node is None:
            return -1
        else:
            left_height=self._height(cur_node.left)
            right_height=self._height(cur_node.right)
            return max(left_height,right_height)+1
    def _simpleHeight(self,cur_node):
        if cur_node is None:
            return 0
        x=self._simpleHeight(cur_node.left)
        y=self._simpleHeight(cur_node.right)
        if x == -1 or y == -1 or abs(x-y) >1:
            return -1
        return max(x,y)+1
    def isBalanced(self):
        if self.root is None:
            return True
        else:
            return self._simpleHeight(self.root)!=-1
    def _isBalanced(self,cur_node):
        if cur_node is None:
            return True
        return self._simpleHeight(cur_node)!=-1


                     

bst=BST()
bst.insert(12).insert(10).insert(6)
print(bst.search(10))
print(bst.contains(17))
print(f"Max {bst.max()}")
print(f"Min {bst.min()}")
print(f"Height {bst.height()}")
print(f"Is balaced {bst.isBalanced()}")