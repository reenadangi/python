class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert(self,value):
        new_node=Node(value)
        if self.head:
            runner=self.head
            while runner.next:
                runner=runner.next
            runner.next=new_node
        else:
            self.head=new_node
        return self
    def insert_front(self,value):
        new_node=Node(value)
        if self.head:
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=new_node
        return self
    # overloading for print 
    # def __repr__(self):
   
        
    def display(self):    
        if self.head:
            runner=self.head
            print('\n')
            while runner:
                print(runner.value)
                runner=runner.next
        return self
    # reverse
# 12 ->13 ->78 ->None
# None<-12 <-13 <-78 head

    def reverse(self):
      if self.head:
        runner=self.head
        prev=None
        while runner:
            next=runner.next
            runner.next=prev 
            prev=runner
            runner=next
        self.head=prev
        return self
    # delete a node
    def delete(self,value):
        if self.head:
            if self.head.value==value:
                self.head=self.head.next
                return self
            runner=self.head
            while runner.next:
                if runner.next.value==value:
                    runner.next=runner.next.next
                    break
                else:
                    runner=runner.next
            return self
    # sort
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
    def get_middle(self,head):
        if head:
            slow=fast=head
        while(fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow
    def sortMerged(self,a,b):
        result = None
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
        # pick either a or b and recur.. 
        if a.value <=  b.value: 
            result = a 
            result.next = self.sortMerged(a.next, b) 
        else: 
            result = b 
            result.next = self.sortMerged(a, b.next) 
        
        return result
        # pick any one list to iterate
        # remove Duplicate
        



    def sort_merge(self,head):
        if head==None or head.next==None:
            return head
        middle=self.get_middle(head)
        nextToMiddle=middle.next
        middle.next=None
        left=self.sort_merge(head)
        right=self.sort_merge(nextToMiddle)
        return self.sortMerged(left,right)
                    
    def sort(self):
        if self.head:
            self.head=self.sort_merge(self.head)
        return self
    # remove duplicate
    def remove_duplicate(self):
            # remove dupliacte from sorted list
        if self.head:
            runner=self.head
            while runner.next:
                if runner.value==runner.next.value:
                        runner.next=runner.next.next
                else:
                    runner=runner.next
        return self

    # insert at
    def insertAtIndex(self,value,index):
        if self.head:
            new_node=Node(value)
            if index==0:
                new_node.next=self.head
                self.head=new_node
            else:
                i=0
                runner=self.head
                while i<index-1 and runner:
                    runner=runner.next
                    i+=1
                if runner:
                    temp=runner.next
                    runner.next=new_node
                    new_node.next=temp
            return self         
                
    def rev(self,head):
        if head:
            runner=head
            prev=None
            while runner:
                next=runner.next
                runner.next=prev
                prev=runner
                runner=next
            return prev
    def isPallindrom(self):
        # travel to half
        # rev sec half
        # compare
        if self.head and self.head.next:
            slow=self.head
            fast=self.head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            #At the end of this while we have the mid point-slow
            sec_half=self.rev(slow)
            first_half=self.head
            # now compare both
            while sec_half and first_half:
                if first_half.value!=sec_half.value:
                    return False
                first_half=first_half.next
                sec_half=sec_half.next
            return True
        else:
            True
                



sll=SLL()
sll.insert(12).insert(13).insert_front(78).display().reverse().display()
sll.delete(13).display()
sll.insert(1).insert(0).insert(0).display().sort().display()
print("remove duplicate")
sll.remove_duplicate().display()
sll.insertAtIndex(66,4).display()
sll2=SLL()
sll2.insert(12).insert(13).insert(13).insert(12).display()
# sll2.insert(30)
print(sll2.isPallindrom())  

       