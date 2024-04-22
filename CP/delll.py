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
        while t:
            print(t.data,end=" ")
            t=t.next
    def delll(self,val):
        t=Node(0)
        t.next=self.head
        prev,curr=t,self.head
        while curr:
            if(curr.data==val):
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return t.next
obj=LinkedList()
n=int(input("enter n : "))
obj.createLL(n)
obj.show(obj.head)
val=int(input("enter the value to be deleted : "))
obj.delll(val)
obj.show(obj.head)
            
                
        
