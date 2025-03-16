def Linkedlist(self,data1,next1=None):
  self.data=data1
  self.next=next1
def insertnode(head,val):
  new_node=Linkedlist(val)
  new_node.next=head
  return new_node

def print(head):
  while head:
    print(head,val, end="->")
    head=head.next
  print("None")
    
