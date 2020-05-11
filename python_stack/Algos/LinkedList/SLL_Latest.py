class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head:
            runner=self.head
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
        return self
    def add_front(self,value):
        if self.head:
            tmp=self.head
            self.head=Node(value)
            self.head.next=tmp
        else:
            self.head=Node(value)
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
    def sortedMerge(self, left, right): 
        l=Node(0)
        runner=l
        while left and right:
            if left.value<right.value:
                left=left.next
            else:
                runner.next=right
                right=right.next
            runner=runner.next
        if left:
            runner.next=left
        if right:
            runner.next=right
        return l.next

        # pick either a or b and recur.. 
        
        # if a.value <= b.value: 
        #     result = a 
        #     result.next = self.sortedMerge(a.next, b) 
        # else: 
        #     result = b 
        #     result.next = self.sortedMerge(a, b.next) 
        # return result 

    def merge_sort(self,runner):
        if not runner or not runner.next:
            return runner
        # devide list in half
        slow,fast=runner,runner.next
      
        # this will give us middle
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        # cut down first
        slow.next=None
        left=self.merge_sort(runner)
        right=self.merge_sort(second)
        return self.sortedMerge(left,right)

    def sort(self):
        if self.head:
            self.merge_sort(self.head)
        return self

                
sll=SLL()
sll.add_last(12).add_last(13).add_front(20).add_front(40).add_last(1).sort().display()



        
        
   