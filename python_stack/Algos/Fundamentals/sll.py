class Node:
    def __init__(self,value=None):
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
    def insert_front(self,value):
        if self.head:
            new_node=Node(value)
            new_node.next=self.head
            self.head=new_node
        return self
    def insert_after(self,value_after,value):
        if self.head:
            runner=self.head
            new_node=Node(value)
            while runner:
                if runner.value==value_after:
                    new_node.next=runner.next
                    runner.next=new_node
                    return self
                else:
                    runner=runner.next
        return self                

    def display(self):
        if self.head:
            runner=self.head
            print("\n")
            while runner:
                print(runner.value)
                runner=runner.next
        return self
    def delete(self,value):
        if self.head:
            runner=self.head
            while runner.next:
                if runner.next.value==value:
                    runner.next=runner.next.next
                else:
                    runner=runner.next
        return self
    def sort(self):
        if self.head:
            runner=self.head
            while runner.next:
                runner2=runner.next
                while runner2:
                    if runner.value>runner2.value:
                        runner2.value,runner.value=runner.value,runner2.value
                    runner2=runner2.next
                runner=runner.next
        return self    

    def remove_duplicate(self):
        if self.head:
            runner=self.head
            while runner.next:
                if runner.value==runner.next.value:
                    runner.next=runner.next.next
                else:
                    runner=runner.next
        return self
      # remove duplicate from unsorted list and keep first instance
    def deDupeList(self):
        # create a new sll and push items if not already there
        if self.head:
            runner=self.head
            new_sll=SLL()
            new_sll.insert(self.head.value)
            while runner:
                new_sll_runner=new_sll.head
                found=False
                while new_sll_runner:
                    if new_sll_runner.value==runner.value:
                        found=True
                        break
                    else:
                        new_sll_runner=new_sll_runner.next
                if not found:
                    new_sll.insert(runner.value)
                runner=runner.next
            self.head=new_sll.head
            return self


                    

sll=SLL()
sll.insert(12).insert(34).insert(90).insert_front(0).insert_after(12,67).display()
sll.delete(90).insert(3).insert(3).insert(67).sort().display()
# remove duplicate from sorted list
print("remove duplicates")
sll.remove_duplicate().display()
sll2=SLL()
sll2.insert(100).insert(400).insert(10).insert(100).display()
sll2.deDupeList().display()


        