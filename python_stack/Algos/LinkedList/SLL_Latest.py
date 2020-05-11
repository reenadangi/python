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
    
sll=SLL()
sll.add_last(12).add_last(13).add_front(10).display()



        
        
   