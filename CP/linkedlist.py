class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def createLL(self,n):
        i=0
        while i<n:
            data=int(input("enter data : "))
            new_node=Node(data)
            if self.head==None:
                self.head=new_node
            else:
                curr_node=self.head
                while curr_node.next!=None:
                    curr_node=curr_node.next
                curr_node.next=new_node
            i=i+1
    def show(self,head):
        t=head
        s=0
        while t:
            print(t.data,end=' ')
            s=s+t.data
            t=t.next
        print("\n")
        print(s)
    def split(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        second=slow
        prev.next=None
        print("First linked list : ")
        self.show(self.head)
        print("Second Linked list : ")
        self.show(second)
obj=LinkedList()
n=int(input("enter number of nodes to be inserted : "))
obj.createLL(n)
obj.show(obj.head)
obj.split()
        
