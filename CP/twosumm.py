class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def create(self,n):
        for d in n:
            new_node=Node(d)
            if self.head==None:
                self.head=new_node
            else:
                curr_node=self.head
                while curr_node.next!=None:
                    curr_node=curr_node.next
                curr_node.next=new_node
    def show(self,m):
        carry=0
        t=self.head
        for d in m:
            if t.next==None:
                print(int(t.val)+int(d)+carry)
            else:
                print((int(t.val)+int(d)+carry)%10)
                carry=(int(t.val)+int(d))//10
            t=t.next
obj=LinkedList()
n=int(input("enter number 1 : "))
m=int(input("eter number 2 : "))
x=str(m)
y=str(n)
obj.create(y)
obj.show(x)
            
            
