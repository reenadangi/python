class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    
    def insert(self,val):
        if self.head:
            runner=self.head
            while runner.next:
                runner=runner.next
            runner.next=Node(val)
        else:
            self.head=Node(val)
        return self
    
    def display(self,head):
        if head:
            runner= head
            while runner:
                print(runner.val)
                runner=runner.next
        return self
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next
    def delete(self,val):
        if self.head:
            runner=self.head
            prev=Node(0)
            prev.next=runner
            runner=prev
            while runner and runner.next:
                if runner.next.val==val:
                    runner.next=runner.next.next
                else:
                    runner=runner.next
            self.head=prev.next
        return self
    def reverseList(self, head):
        if head:
            prev=None
            runner=head
            while runner:
                temp=runner
                runner=runner.next
                temp.next=prev
                prev=temp
            self.head=prev
            return self
    def reverseBetween(self, head, m, n):
        # Reverse a linked list from position m to n. Do it in one-pass.
        # Input: 1->2->3->4->5->NULL, m = 2, n = 4
        # Output: 1->4->3->2->5->NULL
           # Empty list
        if not head:
            return None
        # Move the two pointers until they reach the proper starting point
        # in the list.
        runner, prev = head, None
        while m > 1:
            prev = runner
            runner = runner.next
            m-=1
            n-=1

        # The two pointers that will fix the final connections.
        tail=runner
        con=prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = runner.next
            runner.next = prev
            prev = runner
            runner = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = runner
        return head
    def getIntersectionNode(self, headA, headB):
        if not headA and not headB:
            return None
        pointer1 = headA
        pointer2 = headB
        while pointer1 != pointer2: 
                pointer1 = pointer1.next
                pointer2 = pointer2.next
                if pointer1 == pointer2:
                  return pointer1
                if pointer1 == None:
                  pointer1 = headB
                if pointer2 == None:
                  pointer2 = headA
        return pointer1
        
    def removeZeroSumSublists(self, head):
        dummy=Node(0)
        dummy.next=head
        runner=dummy
        runner2=dummy
        while runner:
            sm=0
            while runner2:
                sm+=runner2.val
                if sm==0:
                    runner.next=runner2.next
                runner2=runner2.next
            runner=runner.next
            if runner:
                runner2=runner.next
        return dummy.next
    
    # Delete N nodes after M nodes of a linked list
    def deleteNnodesAfterM(self,n,m):
        # n=2 , m=2 
        #  1,2,3,4,5,6,7,8
        # output:1,2,5,6,7,8
        if self.head:
            runner=self.head
            i=1
            while i<m:
                runner=runner.next
                i+=1
            print(f"current node is {runner.val}")
            runner2=runner.next
            i=1
            while i<=n:
                runner2=runner2.next
                i+=1
            runner2.next=None
            runner.next=runner2
            return self


      



    def plusOne(self,head):
        if self.head:
             # reverse list
            if self.head.next is None:
                if self.head.val==9:
                    self.head.val=1
                    self.head.next=Node(0)
                    return self
            self=self.reverseList(head)
            # plus one for the first digit
            runner=self.head
            carry=1
            while runner:
                if carry==1:
                    runner.val+=1
                if runner.val>9:
                    runner.val=0
                    carry=1
                    runner=runner.next
                else:
                    carry=0
                    break
            self=self.reverseList(self.head)
            if carry:
                newHead=Node(1)         
                newHead.next=self.head
                self.head=newHead
            return self
    def partition(self, head, x):
        if not head or not head.next: return head
        dummy_left = runner_l = ListNode(0)
        dummy_right = runner_r = ListNode(0)
        runner = head
        while runner:
            if runner.val<x:
                runner_l.next = runner
                runner_l = runner_l.next
            else:
                runner_r.next = runner
                runner_r = runner_r.next
            runner = runner.next

        runner_r.next = None
        runner_l.next = dummy_right.next
        return dummy_left.next
# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
    def hasCycle(self):
        head=self.head
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

    def mergeKLists(lists):
        arr=[]
        for list in lists:
            while list:
                arr.append(list.val)
                list=list.next
        arr.sort()
        head=node=ListNode(-1)
        for i in arr:
            node.next=ListNode(i)
            node=node.next
        return head.next
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head
        
        fast,slow,i=head,head,0
        while fast:
            if i >= n:
                if fast.next:
                    slow=slow.next
                else:
                    slow.next=slow.next.next
            fast=fast.next
            i+=1

        if i==n:
            return head.next
        else:
            return head
    def rotateRight(self, head, k):
        # first connect head to tail so that rotation becomes easy
        # at the same time find the len of linked list
        # new head=lenth-k
        if head:
            runner=head
            l=1
            while runner.next:
                l+=1
                runner=runner.next
            runner.next=head
            k%=l
            if k==0:
                return head
            new_head=l-k
            
            for i in range(new_head,1,-1):
                head=head.next
            runner=head.next
            head.next=None
            return runner
    def addTwoNumbers(self, l1, l2):
        # create a dummy node 
        dummy=cur=Node(0)
        carry=0
        while l1 or l2:
            sum=carry
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            cur.next=Node(sum%10)
            cur=cur.next
            carry=sum//10
        if carry:
            cur.next=Node(carry)
        return dummy.next

            

            
            

#         if not lists:
#             return
#         if len(lists)==1:
#             return lists[0]
#         mid=len(lists)//2
#         l=self.mergeKLists(lists[:mid])
#         r=self.mergeKLists(lists[mid:])
#         return self.merge(l,r)
#     def merge(self,l1,l2):
#         curr=dummy=ListNode(0)
#         while l1 and l2:
#             if l1.val<=l2.val:
#                 curr.next=ListNode(l1.val)
#                 curr=curr.next
#                 l1=l1.next
#             else:
#                 curr.next=ListNode(l2.val)
#                 curr=curr.next
#                 l2=l2.next
#         if l1:
#             curr.next=l1
#         else:
#             curr.next=l2
#         return dummy.next
    
        






sll=SLL()
sll.insert(12).insert(13).insert(15).reverseList(sll.head).display(sll.head)
sll2=SLL()

sll2.insert(1).insert(9).display(sll2.head)
print("PLus one")
sll2.plusOne(sll2.head).display(sll2.head)

# print("Reverse 2")
# sll.insert(120).insert(100).insert(90)
# sll.display(sll.head)
# sll.head=sll.reverseBetween(sll.head,2,4)
# sll.display(sll.head)
# sll4=SLL()
# sll4.insert(1).insert(2).insert(3).insert(-3).insert(4)
# sll4.head=sll4.removeZeroSumSublists(sll4.head)
# print("*****************")
# sll4.display(sll4.head)

# sll5=SLL()
# print("Delete M node after n nodes")

# sll5.insert(1).insert(2).insert(3).insert(4).insert(5).insert(6).deleteNnodesAfterM(2,2).display(sll5.head)
sll6= SLL()
sll6.head=sll6.insert(1).insert(2).insert(3).insert(4).insert(5).insert(6).removeNthFromEnd(sll6.head,2)
sll6.display(sll6.head)

# sll7= SLL()
# sll7.insert(1).insert(2).insert(3).insert(4).insert(5).insert(6).display(sll7.head)
# sll7.head=sll7.rotateRight(sll7.head,2)
# print("Rotated list")
# sll7.display(sll7.head)
# print("Add two list")

# s1=SLL()
# s2=SLL()
# s1.insert(2).insert(4).insert(3)
# s2.insert(5).insert(6).insert(4)
# s1.head=s1.addTwoNumbers(s1.head,s2.head)
# s1.display(s1.head)