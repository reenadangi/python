class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert(self,value):
        if self.head:
            runner=self.head
            while runner.next:
                runner=runner.next
            runner.next=Node(value)
        else:
            self.head=Node(value)
        return self
    
    def display(self):
        if self.head:
            runner=self.head
            print("\n")
            while runner:
                print(runner.value)
                runner=runner.next
        return self

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
    def findMiddle(self,head):
        if head:
            slow=fast=head
            while fast.next and fast.next.next:
                fast=fast.next.next
                slow=slow.next
            return slow
    def merge(self,a,b):
      
        if a==None:
            return b
        if b==None:
            return a
        # pick either a or b 
        result='' 
        if a.value<=b.value:
            result=a
            result.next=self.merge(a.next,b)
        else:
            result=b
            result.next=self.merge(a,b.next)
        return result
            
            
    def _sort(self,head):
        if head==None or head.next==None:
            return head
            middle= self.findMiddle(head)
            nextTomiddle=middle.next
            middle.next=None
            left= self._sort(head)
            right= self._sort(nextTomiddle)
            return self.merge(left,right)
            
    def sort(self):
        if self.head:
            self.head= self._sort(self.head)
            return self
    

    def remove_duplicates(self):
        if self.head:
            runner=self.head
            while runner.next:
                if runner.value==runner.next.value:
                    runner.next=runner.next.next
                else:
                    runner=runner.next
        return self
    def insertAt(self,value,index):
        if self.head:
            new_node=Node(value)
            runner=self.head
            if index==0:
                new_node.next=self.head
                self.head=new_node
                return self
            i=0
            while i<index-1 and runner:
                runner=runner.next
                i+=1
            if runner:
                new_node.next=runner.next
                runner.next=new_node
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
        if self.head:
            slow=self.head
            fast=self.head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            # slow - is pointing at mid point
            sec_half=self.rev(slow)
            first_half=self.head
            # Now we can compare both 
            while first_half and sec_half:
                if first_half.value!=sec_half.value:
                    return False
                first_half=first_half.next
                sec_half=sec_half.next
            return True
        else: return True
    def delete(self,value):
        if self.head:
            runner=self.head
            while runner.next:
                if runner.next.value==value:
                    runner.next=runner.next.next
                    return self
                runner=runner.next
        return self
    def mergeTwo(self,l1,l2):
        if l1==None: return l2
        if l2==None: return l1
        new_node=Node(-1)
        head=new_node
        while l1 and l2:
            if l1.value<=l2.value:
                new_node.next=l1
                l1=l1.next
            else:
                new_node.next=l2
                l2=l2.next
            new_node=new_node.next
        if l1:
            new_node.next=l1
        if l2:
            new_node.next=l2
        self.head=head.next
        return self





            
sll=SLL()
sll.insert(19).insert(13).insert(0).insert(0).insert(19).display()
sll.reverse().display()
sll.remove_duplicates().display()
sll.insertAt(22,0).display()
print(sll.isPallindrom())
sll2=SLL()
sll2.insert(12).insert(13).insert(14).insert(13).insert(12).display()
print(sll2.isPallindrom())
sll2.delete(14).display()
print(sll2.isPallindrom())
sll3=SLL()
sll.display()
sll2.display()
print("after merge")

sll3.mergeTwo(sll.head,sll2.head).display()