import random
class Node:
    def __init__(self,value=10):
        self.value=value
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

# add node at back
    def add_node(self,node):
        if(self.head):
            runner=self.head
            while(runner.next):
                runner=runner.next
            runner.next=node
        else:
            self.head=node
        return self
# add node at front
# [2,44,66,77,88,44] insert 100 at 3rd position
    def add_node_front(self,node):
        if(self.head):
            node.next=self.head
            self.head=node
        return self
# insert_at(self, val, n)
    def insert_at(self,val,n):
        # create a node
        node=Node(val)
        # now insert it at given position 
        if(n==0):
            # insert at first poition and return 
            node.next=self.head
            self.head=node
            return self
        # else do below
        pos=1
        runner=self.head
        while(pos<n):
            runner=runner.next
            pos+=1
        node.next=runner.next
        runner.next=node
        return self

# delete first node- having some value
    def delete_node(self,value):
        runner=self.head
        #  first item is deleted
        if(runner==self.head):
            self.head=runner.next
        else:
            while(runner.next.value!=value):
                runner=runner.next
            print(f"you want to delete {runner.next.value}")
            # check if this is the last item or
            
            if(runner.next.next):
                runner.next=runner.next.next
            else:
                runner.next=None

        return self
#Delete from front 
    def remove_from_front(self):
        # delete front means make next head
        print(f"removing from front{self.head.value}")
        self.head=self.head.next
        return self
#Delete from back 
    def remove_from_back(self):
        # delete from back- iterate till sec last and set next None
        runner=self.head
        while(runner.next.next):
            runner=runner.next
        runner.next=None
        return self
    
#Reverse list
    def reverse_list(self):
        # Store Head->next in a temp
        prv=None
        runner=self.head
        print("In Reversing")
        while(runner):
            temp=runner
            runner=runner.next 
            temp.next=prv
            prv=temp
        self.head=prv
        return self

# Sort List - do with - Merge sort
    def sort_list(self):
       runner=self.head
       while(runner.next):
           runner2=runner.next
           while(runner2):
                    if(runner.value>runner2.value):
                        print("swap")
                        runner.value,runner2.value=runner2.value,runner.value
                    runner2=runner2.next
           runner=runner.next
       return self

# Palindrome Linked List
    def is_Palindrome(self):
        start=self.head

        # find end of the linked list 
        runner=self.head
        while(runner.next.next):
            runner=runner.next
        end= runner
        print (f"start {start.value} end{end.value}")
        # now loop until start.next is end
        
        while(start.next!=end.next):
            if(start.value!=end.next.value):
                return False
            else:
                # increase start and decrease end 
                start=start.next
                

     

# Print all values
    def print_all(self):
        runner=self.head
        while(runner):
            print(runner.value)
            runner=runner.next
        print("*"*40)
        return self
            
# [20,30,60,80,100,120]

node1=Node(random.randint(10,100))
node2=Node(random.randint(10,100))
node3=Node(random.randint(10,100))
node4=Node(random.randint(10,100))
node5=Node(random.randint(10,100))
node6=Node(random.randint(10,100))



my_list=SLL()
my_list.add_node(node1).add_node(node2).add_node(node3).add_node(node4).add_node(node5).add_node(node6)
my_list.print_all()




node7=Node(10)
my_list.add_node_front(node7)
my_list.print_all()

# my_list.delete_node(10)
# my_list.delete_node(120)
# my_list.delete_node(80)

# sort list
my_list.print_all().sort_list().print_all()


# Remove from front
my_list.remove_from_front().print_all()
my_list.remove_from_back().print_all()

# Insert at 
my_list.insert_at(999,4).print_all()
my_list.reverse_list().print_all()


# Make a new linked list and check if that is Palindrome
node7=Node(1)
node8=Node(2)
node9=Node(3)
node10=Node(3)
node11=Node(2)
node12=Node(1)
my_list2=SLL()
my_list2.add_node(node7).add_node(node8).add_node(node9).add_node(node10).add_node(node11).add_node(node12)
my_list2.print_all()
# my_list2.is_Palindrome()