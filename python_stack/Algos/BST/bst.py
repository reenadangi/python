class Node:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,value):
        # add a new node
        if self.root:
            self._insert(self.root,value)
        else:
            self.root=Node(value)
    def _insert(self,cur_node,value):
        # check where to insert left/right
        if cur_node.value>value:
            # insert at left side
            if cur_node.left==None:
                cur_node.left=Node(value)
            else:
                self._insert(cur_node.left,value)

        else:
            # insert at right side
            if cur_node.right==None:
                cur_node.right=Node(value)
            else:
                self._insert(cur_node.right,value)
    def print_tree(self):
        if self.root:
            self._print_tree(self.root)
    def _print_tree(self,cur_node):
        if cur_node:
            self._print_tree(cur_node.left)
            print(cur_node.value)
            self._print_tree(cur_node.right)
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

bst=BST()
bst.insert(12)
bst.insert(13)
bst.insert(10)
bst.insert(14)
bst.insert(16)
bst.insert(15)
bst.insert(3)

bst.print_tree()
print(bst.height())      
       

