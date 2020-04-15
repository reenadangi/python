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
            # call a dunder method with same signature
            self._insert(value,self.root)
        else:
            self.root=Node(value)
    def _insert(self,value,cur_node):
        # Where to insert left/right
        if value<cur_node.value:
            # Insert to left
            # check if there is any left
            if cur_node.left==None:
                # insert here
                cur_node.left=Node(value)
                return
            self._insert(value,cur_node.left)
        else:
            # insert to right
            # check if there is right
            if cur_node.right==None:
                # insert here
                cur_node.right=Node(value)
                return
            self._insert(value,cur_node.right)
            
    def print_tree(self):
        if self.root:
            self._print_tree(self.root)
    
    def _print_tree(self,cur_node):
        # inorder travesal
        if cur_node!=None:
            self._print_tree(cur_node.left)
            print(cur_node.value)
            self._print_tree(cur_node.right)

bst=BST()
bst.insert(12)
bst.insert(10)
bst.insert(15)
bst.print_tree()





  