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
        # left/right
        if cur_node.value>value:
            # insert in left side
            if cur_node.left==None:
                cur_node.left=Node(value)
                
            else:
                self._insert(cur_node.left,value)
        else:
            # insert right side
            if cur_node.right==None:
                cur_node.right=Node(value)
                
            else:
                self._insert(cur_node.right,value)
    def display(self):
        self._display(self.root)
    def _display(self,cur_node):
        if cur_node:
            self._display(cur_node.left)
            print(cur_node.value)
            self._display(cur_node.right)
    def height(self):
        if self.root:
            return self._height(self.root)
        else:
            return -1
    def _height(self,cur_node):
        if cur_node==None:
            return -1
        left_height=self._height(cur_node.left)
        right_height=self._height(cur_node.right)
        return max(left_height,right_height)+1

    def contains(self,value):
            return self._contains(self.root,value)

    def _contains(self,cur_node,value):
        if cur_node==None:
            return False
        if cur_node.value==value:
            return True
        elif cur_node.value>value:
            return self._contains(cur_node.left,value)
        else:
            return self._contains(cur_node.right,value)
    def max(self):
        # travel right most
        if self.root:
            cur_node=self.root
            max=cur_node.value
            while cur_node.right:
                max=cur_node.value
                cur_node=cur_node.right
            return max
    def min(self):
        # travel right most
        if self.root:
            curr_node=self.root
            min=-1
            while curr_node:
                min=curr_node.value
                curr_node=curr_node.left
            return min
        else:
            return False
    
        
bst=BST()
bst.insert(12)
bst.insert(11)
bst.insert(20)
bst.insert(1)
bst.display()
print(bst.height())
print(bst.contains(191))
print(f"Max value in BST is {bst.max()}")
print(f"Minimum value in BST is {bst.min()}")








        