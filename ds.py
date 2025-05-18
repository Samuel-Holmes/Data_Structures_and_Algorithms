# Node example creation OOP 

class Node:

    # constructor function with node_link value defaulted to none

    def __init__(self,value,node_link = None):
        self.value = value 
        self.node_link = node_link

    # define get methods for the objects

    def getvalue(self):
        return self.value

    def get_node_link(self):
        return self.node_link

    # define setter methods 

    def set_value(self, value):
        self.value = value

    def set_node_link(self,node_link):
        self.node_link = node_link


# creating an instance of the node class

node_one = Node(12)
node_two = Node(24)


# linking node_one to node_two 

node_one.set_node_link(node_two)

# checking is set 

check_link = node_one.get_node_link()
check_value = node_one.getvalue()

print(check_link, check_value)

# accessing link data 

value_retrieval = node_one.get_node_link().getvalue()

print(value_retrieval)

"""
!!! TYPES OF LINEAR DATA STRUCTURES !!!

Linked list - a sequentially forward linked set of nodes linear ds head node is at the beginning of the list tail node is at the end of the list 

Doubly linked list - a sequentially forward and backward linked list linear ds

Queue - think of it as an actual queue linked forward as one exits the front another can be added at the back 

Stack - the top item is removed and a new item replaces the top item 
"""

# DEFINING A LINKED LIST AND ITERATING THROUGH IT 


class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  # Define your remove_node method below:

  def remove_node(self, value_to_remove):
    current_node = self.head_node
    
    if self.head_node.get_value() == value_to_remove:
      new_head_node = self.head_node.get_next_node()
      self.head_node.set_next_node(None)
      self.head_node = new_head_node
      
    while current_node.get_next_node() != None:
      
      if current_node.get_next_node().get_value() == value_to_remove:
        current_node.set_next_node(current_node.get_next_node().get_next_node())
        break
      

# DOUBLY LINKED LISTS

"""
Same steps as above but now you include previous and next node link 

Below is a doubly linked list with some basic methods 
"""

class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value


class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head

  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail

  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None

    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()

  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None

    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()

  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break

      current_node = current_node.get_next_node()

    if node_to_remove == None:
      return None

    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)

    return node_to_remove

  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

# Create your subway line here:
subway = DoublyLinkedList()

subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")

print(subway.stringify_list())

subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")

print(subway.stringify_list())

subway.remove_head()
subway.remove_tail()

print(subway.stringify_list())

subway.remove_by_value("Times Square")

print(subway.stringify_list())


# SWAPPING NODES IN A LINKED LIST 

"""
As an example lets say we have values of two nodes val1 and val2
These can correspond to variables called node1 and node2
We would like to swap node1 for node2 but we cannot use an index we will have to iterate through the list 
Following that we need to make sure the pointers are properly assigned for the functionality of the linked list to be maintained 

"""

# Practice below
 
class Node: 
  def __init__(self, value=None, link=None):
    self.value = value
    self.link = link

  def set_val(self, value):
    self.value = value
  
  def get_value(self):
    return self.value

  def set_link(self, link):
    self.link = link
  
  def get_link(self):
    return self.link

class LinkList:
  def __init__(self):
    self.head = None

  def set_head(self, head):
    
    if self.head != None:
      head.set_link(self.head)
      self.head = head
    
    else:
      self.head = head


  def add_to_head(self, node):
    if self.head != None:
      node.set_link(self.head)
      self.head = node
    
    else:
      self.head = node

  def remove_from_head(self):
    if self.head is not None:
      self.head = self.head.get_link()

    

  def remove_by_value(self, value_to_remove):
    # if the list is empty
    if self.head_node is None:
        return

    # if value is at the head
    if self.head_node.get_value() == value_to_remove:
        new_head_node = self.head_node.get_link()
        self.head_node.set_link(None)
        self.head_node = new_head_node
        return

    # Traverse the list
    current_node = self.head_node
    while current_node.get_link() is not None:
        next_node = current_node.get_link()
        if next_node.get_value() == value_to_remove:
            current_node.set_link(next_node.get_link())
            next_node.set_link(None)  
            return
        current_node = current_node.get_link()
      

# defining replace node by value function

  def swap_node_by_value(self,value_to_remove,replacement_node):
    
    if self.head_node is None:
      self.head_node = replacement_node
      return

    if self.head_node.get_value() == value_to_remove:
      replacement_node.set_link(self.head_node.get_link())
      self.head.set_link(None)
      self.head = replacement_node
      return
    
    # traversing the list, replacing node when found and maintaining proper links 

    current_node = self.head_node
    while current_node.get_link() is not None:
      next_node = current_node.get_link()
      if next_node.get_value() == value_to_remove:

    

test = LinkList()
one = Node(20)
two = Node(30)
three = Node(40)
four = Node(50)

