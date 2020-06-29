# insert
# print
# height
# contains
# max
# min
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
    def contains(self,value):
        if self.root:
            return self._contains(self.root,value)
        else:
            return False
    def _contains(self,curr_node,value):
        if curr_node==None:
            return False
        if curr_node.value==value:
            return True
        # value not found  look somewhere else
        if value>=curr_node.value:
            # look right
            return self._contains(curr_node.right,value)
        else:
            # go left
            return self._contains(curr_node.left,value)
    def max(self):
        if self.root:
            curr_node=self.root
            max=-1
            while curr_node:
                max=curr_node.value
                curr_node=curr_node.right
            return max
        else:
            return False
    def min(self):
        if self.root:
            curr_node=self.root
            min=-1
            while curr_node:
                min=curr_node.value
                curr_node=curr_node.left
            return min
        else:
            return False

    def delete(self,value):    
        if self.root:
            self._delete(self.root,value)
    def _delete(self,cur_node,value):
        # Node to be deleted has no child 
        # Node to be deleted has only one child
        # Node to be deleted has two child
       
    
        if cur_node is None:
            return cur_node
       
    #    it is in left subtree
        if value<cur_node.value:
            cur_node.left=self._delete(cur_node.left,value)
        elif value>cur_node.value:
            cur_node.right=self._delete(cur_node.right,value)
        else:
        # value is same , this node need to be remove
        #if there is subchild of the node to be deleted
            if cur_node.left==None and cur_node.right==None:
                cur_node=None
                return cur_node
        # if one child
            elif cur_node.left==None:
                temp=cur_node
                cur_node=cur_node.right
                

            
        
                



bst=BST()
bst.insert(12)
bst.insert(23)
bst.insert(10)
bst.insert(14)
bst.insert(16)
bst.insert(15)
bst.insert(3)
# bst.delete(3)

bst.print_tree()
print(f"height {bst.height()}")  
print(bst.contains(13))    
       

