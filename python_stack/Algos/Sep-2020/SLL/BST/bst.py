class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
class BST:
    def __init__(self):
        self.root=None
        self.tilt=0
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
    def findTilt(self):
        if(self.root == None and (self.root.left==None and self.right==None)):
             return self.tilt
        self._findTilt(self.root)
        return self.tilt

    def _findTilt(self, cur_node):
       if cur_node==None: return 0
       left = self._findTilt(cur_node.left)
       right = self._findTilt(cur_node.right)
       self.tilt+=abs(left - right)
       return left+right+cur_node.value
                     
    def zigzagLevelOrder(self, root):
        if not root: return []
        out=[]
        stack1,stack2=[root],[]
        while stack1 or stack2:
            while stack1:
                node=stack1.pop()
                out.append(node.value)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            while stack2:
                node=stack2.pop()
                out.append(node.value)
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
        return out
    # Time Complexity:  O(n+m)
    # Space complexity: O(n+m)

    def inOrderTraversal(self):
        if self.root:
            lst=[]
            return self._inOrderTraversal(self.root,lst)
           
    def _inOrderTraversal(self,cur_node,lst):
        if not cur_node:
            return lst
        self._inOrderTraversal(cur_node.left,lst)
        lst.append(cur_node.value)
        self._inOrderTraversal(cur_node.right,lst)
        return lst
    def _inOrderCheck(self,root,lst):
        if root is None: return True
        if not self._inOrderCheck(root.left,lst):
            return False

        if not lst or lst[0]!=root.value:
            return False
        del lst[0]       
        return  self._inOrderCheck(root.right,lst)
            
    def preOrderTravelsal(self,root):
        # Data left right 
        if root:
            print(root.value)
            self.preOrderTravelsal(root.left)
            self.preOrderTravelsal(root.right)
    
    def postOrder(self,root):
        # left right Data
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.value)
        
                
                



     







bst=BST()
bst.insert(9).insert(3).insert(20).insert(15).insert(7).insert(2).insert(25)
print(f"Tilt: {bst.findTilt()}")
print(bst.search(10))
print(bst.contains(17))
print(f"Max {bst.max()}")
print(f"Min {bst.min()}")
print(f"Height {bst.height()}")
print(f"Is balaced {bst.isBalanced()}")

bst.display()
print(bst.zigzagLevelOrder(bst.root))

lst1=bst.inOrderTraversal()
bst2=BST()
bst2.insert(9).insert(20).insert(3).insert(15).insert(7).insert(2).insert(25)
lst2=bst2.inOrderTraversal()
if lst1==lst2:
    print("Yes")
else:
    print("Oh! no")
print(bst2._inOrderCheck(bst2.root,lst1) and len(lst1)==0) 
print(f"Pre Order:")
bst2.preOrderTravelsal(bst2.root)
print(f"Post Order:")
bst2.postOrder(bst2.root)