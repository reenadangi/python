class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def addNode(self,node):
        if(self.head):
            runner=self.head
            while(runner.next):
                runner=runner.next
            runner.next=node
        else:
            self.head=node
        return self
    def displaySll(self):
            runner=self.head
            print("*"*20)
            while(runner):
                print(runner.value)
                runner=runner.next
            print("*"*20)
            return self
    # add node at front
# [2,44,66,77,88,44] insert 100 at 3rd position
    def addnode_front(self,new_node):
        # add node in front
        new_node.next=self.head
        self.head=new_node
        return self
    def insert_at(self,val,n):
        # insert val at given location
        new_node=Node(val)
        pos=1
        runner=self.head
        while(pos<n):
            print("in insert at")
            pos=pos+1
            runner=runner.next
        new_node.next=runner.next
        runner.next=new_node
        return self
        
    # delete first node
    def delete_first_node(self):
        # make sec node as head
        if(self.head.next):
            self.head=self.head.next
        return self
    #Delete from back 
    def delete_last_node(self):
        runner=self.head
        while(runner.next.next):
            runner=runner.next
        runner.next=None
        return self
    # sort
    def sort_list(self):
        runner=self.head
        while(runner):
            runner2=runner.next
            while(runner2):
                if(runner.value>runner2.value):
                    print("Swap")
                    runner.value,runner2.value=runner2.value,runner.value
                runner2=runner2.next
            runner=runner.next
        return self
    # contains
    def contains(self, value):
        runner=self.head
        while(runner):
            if runner.value==value:
                return True
            runner=runner.next
        return False
    def max(self):
        max_val=self.head.value
        runner=self.head
        while(runner):
            if max_val<runner.value:
                max_val=runner.value
            runner=runner.next
        return max_val                    

#SList: Prepend Val
# Create prependVal(ListNode,val,before) to insert a new ListNode with 
# val immediately before the node containing before (or at end, if no node contains before ). 
# Return the new list.
# prepend 4 before 6
#  2,3,6,7,8,9
    def prependVal(self,val,before):
        new_node=Node(val)
        if(self.head.value==before):
            # insert value at head
            print(f"prepend {val} before {before}")
            return self.addnode_front(new_node)
        runner=self.head
        while(runner.next.value!=before):
            runner=runner.next
       
        temp=runner.next
        runner.next=new_node
        new_node.next=temp
        return self
    # append 10 after 8 
    #  2,3,6,7,8,9
    def appendVal(self,val,after):
        runner=self.head
        while(runner.value!=after):
            runner=runner.next
        if runner.value==after:
            new_node=Node(val)
            new_node.next=runner.next
            runner.next=new_node
        return self

    def mergeSll(self,l1,l2):
        # merge self and l2
        if l1 is None : 
            return l2
        if l2 is None : 
            return l1
        
        new_node=Node(None)
        new_sll=SLL()
        new_sll.head=new_node
        while(l1 and l2):
            if l1.value<l2.value:
                new_node.next=l1
                l1=l1.next
            else:
                new_node.next=l2
                l2=l2.next 
            new_node=new_node.next
        if l1:
            new_node.next=l1
        else:
            new_node.next=l2  
        return new_sll.head.next
        
    def remove_duplicate(self):
        runner=self.head
        while(runner):
            if runner.value==runner.next.value:
                # fix the link
                runner.next=runner.next.next
            runner=runner.next
            
        return self
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        fast=head.next
        slow=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False
    # reverse_list
    def reverse_list(self,head):
        prev=None
        cur=head
        while cur:
            next_node=cur.next
            cur.next=prev
            prev,cur=cur,next_node
        return prev

    #  Palindrome Linked List
    def is_Palindrome(self):
        if self.head and self.head.next:
            head=self.head
            slow=head
            fast=head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            # At the end of this while - we have slow at mid point
            # Now reverse second half
            sec_half=self.reverse_list(slow)
            # sec_half.displaySll()
            first_half=head
            # Now compare both halfs
            while sec_half and first_half:
                if first_half.value!=sec_half.value:
                    return False
                first_half=first_half.next
                sec_half=sec_half.next
            return True
        else:
            return True




node1=Node(100)
node2=Node(190)
node3=Node(40)
node4=Node(133)
my_list=SLL()
my_list.addNode(node1).addNode(node2).addNode(node3).addnode_front(node4).insert_at(33,2).sort_list().displaySll()
print(f'Max Value in list{my_list.max()}')
print("deleting first & last node")
my_list.delete_first_node().delete_last_node().sort_list().displaySll()
  
# my_list.prependVal(88,33).prependVal(189,100).appendVal(190,88).displaySll()
# print(my_list.contains(133))

your_list=SLL()
node3=Node(70)
node4=Node(200)
node5=Node(490)
your_list.addNode(node3).addNode(node4)

n1=Node(1)
n2=Node(2)
n3=Node(4)
n4=Node(5)

n5=Node(3)
n6=Node(9)
n7=Node(9)
l1=SLL()

l1.addNode(n1).addNode(n2).addNode(n3).addNode(n4)
l2=SLL()
l2.addNode(n5).addNode(n6).addNode(n7)
new_list=SLL()
new_list.head=my_list.mergeSll(l1.head,l2.head)
print("Merged List")
new_list.displaySll()
print("Remove Duplicate")
new_list.remove_duplicate().displaySll()
print(f"This list has cycle -{new_list.hasCycle(new_list.head)}")


# Make a new linked list and check if that is Palindrome
node7=Node(1)
node8=Node(2)
node9=Node(3)
node10=Node(3)
node11=Node(2)
node12=Node(1)
my_list2=SLL()
my_list2.addNode(node7).addNode(node8).addNode(node9).addNode(node10).addNode(node11).addNode(node12)
my_list2.displaySll()
print(f"This list is Palindrome {my_list2.is_Palindrome()}")

node13=Node(1)
node14=Node(2)
my_list3=SLL()
my_list3.addNode(node13).addNode(node14)
print(f"This list is Palindrome {my_list3.is_Palindrome()}")
