class Node:
  def __init__(self,data):
    self.data = data
    self.next =  None

class Linkedlist:
  def __init__(self):
    self.head = None
  
  def push(self,new_data):
    new_node =  Node(new_data)
    new_node.next = self.head
    self.head = new_node
  
  def insertAfter(self,prev_node,new_data):
    if(prev_node is None):
      print("Prev node must be in the list")
      return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node
  
  def append(self,new_data):
    new_node = Node(new_data)
    if (self.head is None):
      self.head = new_node
      return
    last = self.head
    while(last.next):
      last = last.next
    last.next = new_node

  def printList(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next

  def deleteNode(self,position):
    if (self.head == None):
      return 
    
    temp = self.head
    if(position==0):
      self.head = temp.next
      temp = None
      return 
    
    for i in range(position-1):
      temp = temp.next
      if(temp is None):
        return 
    
    if temp is None:
      return 
    if temp.next is None:
      return
    next  = temp.next.next
    temp.next = None
    temp.next = next
  def getCountrec(self,node):
    if(not node):
      return 0
    else:
      return 1 + self.getCountrec(node.next)
  
  def getCount(self):
    return self.getCountrec(self.head)
  

  def search(self,x):
    current = self.head
    while(current!=None):
      if(current.data == x):
        return True
      current = current.next
    return False

  def searchRec(self,li,key):
    if(not li):
      return False
    if(li.data == key):
      return True
    return self.searchRec(li.next,key)



if __name__ == '__main__':
  llist = Linkedlist()
  llist.append(6)
  llist.push(4)
  llist.push(3)
  llist.insertAfter(llist.head.next.next,5)
  llist.deleteNode(1)
  llist.append(7)
  llist.append(10)
  llist.printList()
  if((llist.searchRec(llist.head,10))):
    print("ELement in the list")
  print('the length of the list is ',llist.getCount())