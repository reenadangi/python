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


bst=BST()
bst.insert(12).insert(10).insert(16).insert(11).display()
print(bst.search(10))
print(bst.contains(17))