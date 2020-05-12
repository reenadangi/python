class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.size = 0
    def display(self):
        if self.head:
            runner=self.head
            print("Display linked list")
            while runner:
                print(runner.value)
                runner=runner.next
        return self
    def add_last(self,value):
        if self.head:
            runner=self.head
            while runner.next:
                runner=runner.next
            runner.next=Node(value)
        else:
            self.head=Node(value)

        self.size+=1
        return self
    def add_front(self,value):
        if self.head:
            tmp=self.head
            self.head=Node(value)
            self.head.next=tmp
        else:
            self.head=Node(value)
        self.size+=1
        return self
    def pop(self):
        # pop value from last 
        if self.head :
            if not self.head.next:
                # remove head
                self.head=None
                return
            runner=self.head
            prev=runner
            while runner.next:
                prev=runner
                runner=runner.next
            prev.next=None
            self.size+=1
            return self
    def len(self):
        i=0
        runner=self.head
        while runner:
            i+=1
            runner=runner.next
        return i
    def addAtIndex(self,index,val):
        # add value at perticular index value before the given index
        if index < 0 or index > self.size:
            return
        if self.head:
            i=0
            runner=self.head
            prev=-1
            print(self.len())
            while(i<index and runner):
                prev=runner
                runner=runner.next
                i+=1
            print(f"insert at {i} after {prev.value}")
            new_node=Node(val)
            new_node.next=prev.next
            prev.next=new_node
        return self





    # def sort(self):
    #     if self.head:
    #         runner=self.head
    #         while runner.next:
    #             runner2=runner.next
    #             while runner2:
    #                 if runner.value>runner2.value:
    #                     runner.value,runner2.value=runner2.value,runner.value
    #                 runner2=runner2.next
    #             runner=runner.next
    #     return self
    # merge sort
    def getMiddle(self,head):
        if head:
            slow=fast=head
        while(fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow
    def sortedMerge(self, a, b): 
        result = None
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
        # pick either a or b and recur.. 
        if a.value <= b.value: 
            result = a 
            result.next = self.sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = self.sortedMerge(a, b.next) 
        
        return result
    def merge_sort(self,head):
        if head==None or head.next==None:
            return head
        middle=self.getMiddle(head)
        nextToMiddle=middle.next
        middle.next=None
        left=self.merge_sort(head)
        right=self.merge_sort(nextToMiddle)
        return self.sortedMerge(left,right)
    def sort(self):
        if self.head:
            self.head=self.merge_sort(self.head)
        return self
    def reverse(self,head):
        if head:
            runner=head
            prev=None
            while runner:
                temp=runner
                runner=runner.next
                temp.next=prev
                prev=temp
            head=prev
        return head
    def reorder(self):
        # first find middle
        # Split it in two parts
        # reverse second half
        # zip first and reversed second half

        if self.head:
            # find middle
            middle=self.getMiddle(self.head)
            print(f"middle:{middle.value}")
            nextToMiddle=middle.next
            middle.next=None
            # reverse sec half
            nextToMiddle=self.reverse(nextToMiddle)
            # zip both the half
            new_node=self.head
            while nextToMiddle:
                tmp1=new_node.next
                tmp2=nextToMiddle.next
                new_node.next=nextToMiddle
                nextToMiddle.next=tmp1
                new_node=tmp1
                nextToMiddle=tmp2
            



                
sll=SLL()
sll.add_last(12).add_last(13).add_front(20).add_front(40).add_last(1)
sll.sort()
sll.display()
sll.addAtIndex(5,4)
# sll.pop()
sll.display()
sll.head=sll.reverse(sll.head)
sll.display()
sll.reorder()
sll.display()
sll2=SLL()
sll2.add_last(1).add_last(2).add_last(3).add_last(4).add_last(5).add_last(6).add_last(7).add_last(8)
sll2.reorder()
sll2.display()


        
        
   