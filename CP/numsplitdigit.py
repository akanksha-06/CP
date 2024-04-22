class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def createLL(self,n):
        for d in n:
            new_node=Node(d)
            if self.head==None:
                self.head=new_node
            else:
                curr_node=self.head
                while curr_node.next!=None:
                    curr_node=curr_node.next
                curr_node.next=new_node
    def show(self,head):
        t=head
        while t:
            print(t.data,end=" ")
            t=t.next
obj=LinkedList()
n=int(input("enter a number : "))
x=str(n)
obj.createLL(x)
obj.show(obj.head)

        
