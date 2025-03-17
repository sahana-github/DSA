class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def insert(self,data):
    new_node=Node(data)
    if not in self.head:
      self.head=new_node
      return
    temp=self.head
    while temp.next:
      temp=temp.next
    temp.next=new_node
  def display(self):
    temp=self.head
    while temp:
      print(temp.data,end="->")
      temp=temp.next
    print("None")
l1=Linkedist()
l1.insert(10)
l1.insert(20)
l1.display()
    
