 def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ##Merge 2 lists into new list. 
        def merge(l1,r1):
            d_head = ListNode(0)
            current = d_head
            
            while l1 and r1:
                if l1.val < r1.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = r1
                    r1 = r1.next
                current= current.next
            current.next = l1 or r1
            return d_head.next
                
        ##Divide the list until list has one or no element,
        ##if head == None (no element) , if head.next= None (one element)
        def mergesort(head):
            if not head or not head.next:
                return head
            
            slow = head
            fast = head
            temp = head
            while fast and fast.next:
                temp = slow
                slow = slow.next
                fast = fast.next.next
            temp.next = None
            
            left = mergesort(head)
            right = mergesort(slow)
            return merge(left,right)
        
        return mergesort(head)
		