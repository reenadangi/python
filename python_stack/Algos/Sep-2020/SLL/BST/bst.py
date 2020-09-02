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
        if self.root:
            self._display(self.root)
    def _display(self,cur_node):
        if cur_node:
            self._display(cur_node.left)
            print(cur_node.value)
            self._display(cur_node.right)
bst=BST()
bst.insert(12).insert(10).insert(16).insert(11).display()
