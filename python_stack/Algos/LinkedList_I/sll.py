# Reverse Linke List
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL:
    def __init__(self):
       self.head=None
    # insert value at the end
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
            while runner:
                print(runner.value)
                runner=runner.next
        return self
    # insert Value at front
    def insert_front(self,value):
        if self.head:
            new_node=Node(value)
            new_node.next=self.head
            self.head=new_node
        return self
    # reverse SLL
    def reverse_sll(self):
        if self.head:
            runner=self.head
            prev=None
        while runner:
            temp=runner
            runner=runner.next
            temp.next=prev
            prev=temp
        self.head=prev
        return self
    # remove duplicate from unsorted list and keep first instance
    def deDupeList(self):
        if self.head:
            runner=self.head
            new_sll=SLL()
            new_sll.insert(self.head.value)
            while runner:
                found=False
                new_sll_runner=new_sll.head
                while new_sll_runner:
                    if runner.value == new_sll_runner.value:
                        found=True
                        break
                    new_sll_runner=new_sll_runner.next
                if not found:
                    new_sll.insert(runner.value)    
                runner=runner.next
       
        self.head=new_sll.head
        
        return self

    #Sort linked list
    def sort(self):
        if self.head:
            runner=self.head
            while runner.next:
                runner2=runner.next
                while runner2:
                    if runner.value>runner2.value:
                        # swap
                        runner2.value,runner.value=runner.value,runner2.value
                    runner2=runner2.next
                runner=runner.next
        return self

    # remove duplicate from sorted list
    def remove_duplicate(self):
        # sort 
        return self

    def kthlast(self,k):
        len=0
        if self.head:
            runner=self.head
            while runner:
                len+=1
                runner=runner.next
            runner=self.head
            for i in range(0,len-k):
                runner=runner.next
            return runner.value
    def rev(self,head):
        prev=None
        cur=head
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev
    def isPalindrome(self,head):
        if head and head.next:
            slow=head
            fast=head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            #At the end of this while we have the mid point-slow
            sec_half=self.rev(slow)
            first_half=head
            # now compare both   
            while sec_half and first_half:
                if first_half.value!=sec_half.value:
                    return False
                first_half=first_half.next
                sec_half=sec_half.next
            return True
        else:
            True
    # delete last element
    def pop(self):
        if self.head:
            runner=self.head
            while runner.next.next:
                runner=runner.next
            runner.next=None
        return self
        
        
sll=SLL()
sll.insert(12).insert(18).insert(50).insert(10).insert(10).insert_front(10).reverse_sll().deDupeList().sort()
sll.display()
print(f"3rd last item in list is {sll.kthlast(3)}")
sll2=SLL()
sll2.insert(10).insert(12).insert(12).insert(10)
# work on this
# print(sll.isPalindrome(sll.head))
# print(sll2.isPalindrome(sll2.head))
sll.pop().display()
sll2.pop().display()