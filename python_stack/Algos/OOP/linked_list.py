class Node:
    def __init__(self,value):
       self.value=value
       self.next=None
class SLL:
    def __init__(self):
      self.head=None
    # add node at back
    def addNode(self,node):
        if self.head:
            runner=self.head
            while runner.next:
                runner=runner.next 
            runner.next=node
        else:
            self.head=node
        return self
    def display(self):
        if self.head:
            runner=self.head
            while(runner):
                print(runner.value)
                runner=runner.next
        return self
    def addNodeFront(self,node):
        if self.head:
            temp=self.head
            self.head=node
            self.head.next=temp
        else:
            self.head=node
        return self
        # remove from front
    def remove(self):
        if self.head.next:
            self.head=self.head.next
        else:
            self.head=None
        return self
    def removeLastNode(self):
        if self.head:
            runner=self.head
            while(runner.next):
                runner=runner.next
            runner.next=None
        return self
        
    # method overriding 
    def remove(self,value):
        if self.head:
            runner=self.head
            if runner.value==value:
                # First Node Found - delete
                self.head=self.head.next
                return self
            else:
                while(runner.next):
                    if runner.next.value==value:
                        runner.next=runner.next.next
                        return self
                    else:
                        runner=runner.next
            return self
        # Reverse a linked list
    def reverse(self):
        if self.head:
            print("IN REVERSE")
            prev=None
            runner=self.head
            while(runner):
                temp=runner
                runner=runner.next
                temp.next=prev
                prev=temp 
            self.head=prev
        return self
        # Do it with merge sort
    def sort(self):
        if self.head:
            print("Sort")
            runner=self.head
            while runner.next:
                runner2=runner.next
                while runner2:
                    if runner.value>runner2.value:
                        runner.value,runner2.value=runner2.value,runner.value
                    runner2=runner2.next
            runner=runner.next
        return self

# Middle of the Linked List
# If there are two middle nodes, return the second middle node.
    def middle(self):
        if self.head:
            slow=self.head
            fast=self.head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            print (f"Middle:{slow.value}")

    def max(self):
        if self.head:
            max=self.head.value
            runner=self.head
            while runner:
                if max<runner.value:
                    max=runner.value
                runner=runner.next
            print(f"MAX {max}")
        return self
    # Next Greater Node In Linked List
    def next_greater(self):
        if self.head:
            runner=self.head
            while(runner.next):
                runner2=runner.next
                while(runner2):
                    if runner.value<runner2.value:
                        runner.value=runner2.value
                        break
                    runner2=runner2.next
                if not runner2:
                    runner.value=0
                runner=runner.next
            return self
                                
    # Merge 2 sorted list
    def merge_sorted(self,sll2):
        if self.head is None:
            return sll2
        if sll2.head is None:
            return self
        l1=self.head
        l2=sll2.head
        new_node=Node(-1)
        head=new_node
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
        elif l2:
            new_node.next=l2
        return new_node.next
             
    def odd_even_list(self):
        print("In Odd even")
        if self.head and self.head.next:
            tmpnode=self.head.next
            odd=self.head
            even=self.head.next
            while odd.next and even.next:
                odd.next=odd.next.next
                odd=odd.next
                even.next=even.next.next
                even=even.next
            odd.next=tmpnode
            return self
        else:
            return self    

node1=Node(100)
node2=Node(200)
sll=SLL()
sll.addNode(node1).addNode(node2).addNodeFront(Node(80)).addNode(Node(67)).remove(200).remove(80).addNode(Node(4)).addNode(Node(14)).display().reverse().display()


# sll.middle()            
# sll.max()
# sll.next_greater().display()
# sll2=SLL()
# sll3=SLL()
# sll2.addNode(Node(2)).addNode(Node(3)).addNode(Node(9))
# sll3.addNode(Node(1)).addNode(Node(4)).addNode(Node(8))
# sll4=sll2.merge_sorted(sll3)
# sll.display()
newSll=SLL()
newSll.addNode(Node(1)).addNode(Node(2)).addNode(Node(3)).addNode(Node(4)).addNode(Node(5)).display()
newSll.odd_even_list().display()
sll.odd_even_list().display()