class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None

  def insert(self,data):
    new_node=Node(data)
    if not self.head:
      self.head=new_node
      return
    temp=self.head
    while temp.next:
      temp=temp.next
    temp.next=new_node

  def delete(self,key):
    temp=self.head:

    #case 1: if node to be deleted is head
    if temp and temp.data==key:
      self.head=temp.next
      temp=None
      return

    #case 2: if its in middle
    prev=None
    while temp and temp.data!=key:
      prev=temp
      temp=temp.next

    if not temp:
      print("key not found")

    def display(self):
      temp=self.head
      while temp:
        print(temp.data,end="->")
        temp=temp.next
      print("None")
l1=Linkedlist()
l1.insert(10)
l1.delete(10)
l1.display()
      
      
