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
    def palindrome(self):
        if self.head is None:
            return True
        slow=self.head
        fast=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        prev=None
        curr=slow
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        first=self.head
        second=prev
        while first:
            if first.data!=second.data :
                return False
            first=first.next
            second=second.next
        return True
obj=LinkedList()
n=int(input("enter number of nodes to be inserted : "))
obj.createLL(n)
obj.show(obj.head)
print(obj.palindrome())
