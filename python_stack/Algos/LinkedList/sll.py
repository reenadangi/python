class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class Sll:
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
    def insertAtFront(self,value):
        if self.head:
            temp=self.head
            self.head=Node(value)
            self.head.next=temp
        return self
    def insertAfter(self,after,value):
        if self.head:
            runner=self.head
            while runner:
                if runner.value==after:
                    node=Node(value)
                    node.next=runner.next
                    runner.next=node
                    return self
                runner=runner.next
            return self
    def insertAtLast(self,value):
        if self.head:
            runner=self.head
            while runner.next:
                runner=runner.next
            runner.next=Node(value)
            return self
    def display(self):
        if self.head:
            runner=self.head
            while runner:
                print (runner.value)
                runner=runner.next
        return self
    def delete(self,value):
        if self.head:
            if self.head.value==value:
                # remove head and make next head
                self.head=self.head.next
                return
            runner=self.head
            while runner.next:
                if runner.next.value==value:
                    runner.next=runner.next.next
                    return
                runner=runner.next
    def length(self):
        len=0
        if self.head:
            runner=self.head
            while runner:
                len+=1
                runner=runner.next
        return len
    def reverseSll(self):
        # reversing a link list can be tricky as you have to make end as head
        if self.head:
            runner=self.head
            prev=None
            while runner:
                # next=runner.next
                # runner.next=prev
                # prev=runner
                # runner=next
                temp=runner
                runner=runner.next
                temp.next=prev
                prev=temp
            self.head=prev
        return self
    def getMiddle(self, head): 
        if (head == None): 
            return head 
        slow = head 
        fast = head 
        while (fast.next != None and 
               fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
        return slow 
    def merge(self,a,b):
        result = None
          
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
              
        # pick either a or b and recur.. 
        if a.value <= b.value: 
            result = a 
            result.next = self.merge(a.next, b) 
        else: 
            result = b 
            result.next = self.merge(a, b.next) 
        return result 
    def mergeSort(self,h):
        # Base case if head is None 
        if h == None or h.next == None: 
            return h 
  
        # get the middle of the list  
        middle = self.getMiddle(h) 
        nexttomiddle = middle.next
  
        # set the next of middle node to None 
        middle.next = None
  
        # Apply mergeSort on left list  
        left = self.mergeSort(h) 
          
        # Apply mergeSort on right list 
        right = self.mergeSort(nexttomiddle) 
  
        # Merge the left and right lists  
        sortedList= self.merge(left, right) 
        return sortedList 
    def sort(self):
        if self.head:
            runner=self.head
            while runner.next:
                runner2=runner.next
                while runner2:
                    if runner.value>runner2.value:
                        # swap
                        runner.value,runner2.value=runner2.value,runner.value
                    runner2=runner2.next
                runner=runner.next
            return self
    def mergeTwo(self,l1,l2):
        if l1==None: return l2
        if l2==None: return l1
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
        if l2:
            new_node.next=l2
        self.head=head.next
        return self
    def mergRec(self,l1,l2):
        if not (l1 and l2):
            return l1 or l2
        if l1.value > l2.value:
            l1, l2 = l2, l1
        l1.next = self.mergRec(l1.next, l2)
        self.head=l1
        return l1
    # def removeNthFromEnd(self,n):
    #     if n==0:
    #         return self
    #     if self.head:
    #         fast=self.head
    #         slow=self.head
    #         i=0
    #         while fast:
    #             if i>=n:
    #                 if fast.next:
    #                     slow=slow.next
    #                 else:
    #                     slow.next=slow.next.next
    #             fast=fast.next
    #             i+=1
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
    def oddEven(self):
        if self.head and self.head.next:
            temp=self.head
            odd=self.head
            even=self.head.next
            while odd and even:
                odd.next=odd.next.next
                odd=odd.next
                even.next=even.next.next
                even=even.next
            odd.next=temp
            return self
        return self
    def nextLargerNode(self,head):
        runner=head
        self.head=self.head.next
        while(runner.next):
            runner=runner.next
        print(f"Last node{runner.value}")
        runner.next=Node(0)
        runner.next.next=None
        return self
    def deleteDuplicates(self,head):
        temp=self.head
        if temp==None:
            return
        while temp.next is not None:
            if temp.value==temp.next.value:
                new=temp.next.next
                temp.next=new
            else:
                temp=temp.next
        return self
    def deleAllDuplicates(self,head):
        runner=head
        head = pre = Node(0)
        head.next = runner
        pre.next=runner
        while runner and runner.next:
            if runner.value == runner.next.value:
                while runner and runner.next and runner.value == runner.next.value:
                    runner = runner.next
                runner = runner.next
                pre.next = runner
            else:
                pre = pre.next
                runner = runner.next
        return head.next
    def rotateRight(self,head,k):
        if head is None:
            return None
        if head.next and k==0 is None:
            return head
        length=1
        runner=head
        while(runner.next):
            length+=1
            runner=runner.next
        rotateTimes=k%length
        if rotateTimes==0:
            return head
        slow=head
        fast=head
        for i in range(rotateTimes):
            fast=fast.next
        while(fast.next):
            slow=slow.next
            fast=fast.next
        temp=slow.next
        slow.next=None
        fast.next=head
        head=temp
        return head
    def removeFromBack(self):
        val=None
        if self.head:
            if self.head.next==None:
                # remove head
                val=self.head.value
                self.head=None
                return val
            else:
                runner=self.head
                while(runner.next):
                    if runner.next.next==None:
                        # remove runner.next
                        val=runner.next.value
                        runner.next=None
                        return val
                    else:
                        runner=runner.next
        return False        
    def insert_at(self, val, n):
        # insert at nth position
        if self.head:
            if n==0:
                tmp=self.head.next
                self.head=Node(val)
                self.head.next=tmp
            else:
                runner=self.head
                i=1
                while(i<n and runner.next):
                    i+=1
                    runner=runner.next
                tmp=runner.next
                runner.next=Node(val)
                runner.next.next=tmp



        


sll=Sll()
sll.insert(120)
sll.insert(13)
sll.insert(6)
sll.insert(20)
sll.insert(22)
sll.insertAtFront(2)
sll.insertAfter(13,100)
sll.insertAtLast(123)
sll.delete(100)
sll.display()

sll.reverseSll()
print("after rev")
sll.display()
print("After Sort")
sll.sort().display()
# merge sort not working 
# sll.mergeSort(sll.head)
print("After Sort")
sll.display()
sll2=Sll()
sll2.insert(0)
sll2.insert(3)
sll2.insert(16)
sll2.insert(200)
sll2.sort()
print("*"*12)
# sll2.display()
# sll.display()
sll.mergeTwo(sll.head,sll2.head).display()

sll3=Sll()
sll3.insert(2)
sll3.insert(22)
sll3.insert(22)
sll3.insert(2)
sll3.insert(67)
print(sll3.isPalindrome(sll3.head))
print("####")
sll.sort().display()
# sll=sll.mergRec(sll.head,sll2.head)

# print(sll.length())

# sll.removeNthFromEnd(2)

print("##########")
sll4=Sll()
sll4.insert(15)
sll4.insert(5)
sll4.insert(5)
sll4.insert(17)
sll4.insert(10)
sll4.insert(25)
sll4.insert(3)
print("********")
sll4.sort().display()
# sll4.sort().display()
# sll4.nextLargerNode(sll.head).display()
print("********")
# sll4.deleteDuplicates(sll4.head).display()
sll4.head=sll4.deleAllDuplicates(sll4.head)
sll4.display()
print("**********")
# print("delete",sll4.removeFromBack())
# print("delete",sll4.removeFromBack())
# print("delete",sll4.removeFromBack())
# print("delete",sll4.removeFromBack())
# print("delete",sll4.removeFromBack())
# print("delete",sll4.removeFromBack())

sll4.insert_at(28,1)
print("%%%%")
sll4.display()





        