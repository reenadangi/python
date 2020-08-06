class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
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

    def display(self):
        if self.root:
            self._display(self.root)
    def _display(self,cur_node):
        # inorder travelsal
        if cur_node:
            self._display(cur_node.left)
            print(cur_node.value)
            self._display(cur_node.right)
    def max(self):
        if self.root:
            max=0
            cur_node=self.root
            while cur_node:
                max=cur_node.value
                cur_node=cur_node.right
            return max
    def min(self):
        if self.root:
            min=0
            cur_node=self.root
            while cur_node:
                min=cur_node.value
                cur_node=cur_node.left
            return min
    def contains(self,value):
        if self.root:
            return self._contains(self.root,value)
    def _contains(self,cur_node,value):
        if cur_node==None:
            return False
        else:
            if cur_node.value==value:
                return True
            if cur_node.value>value:
                # look left
                return self._contains(cur_node.left,value)
            elif cur_node.value<value:
                return self._contains(cur_node.right,value)
            

           
           


bst=BST()
bst.insert(12).insert(14).insert(10).insert(90).display()
print("max:")
print(bst.max())
print(bst.height())
print("min:")
print(bst.min())
print(bst.contains(128))
