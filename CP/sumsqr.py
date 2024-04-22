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
    def oddeven(self,head):
        oddhead=head
        evenhead=head.next
        odd=oddhead
        even=evenhead
        while even and even.next:
            
            odd.next=even.next
            odd=odd.next
            odd.data=odd.data*odd.data
            even.data=even.data+even.data
            even.next=odd.next
            even=even.next
            
        odd.next=evenhead
        self.show(self.head)
            
    def show(self,head):
        t=head
        while t:
            print(t.data,end=" ")
            t=t.next
obj=LinkedList()
n=int(input("enter n:"))
obj.createLL(n)
obj.oddeven(obj.head)
