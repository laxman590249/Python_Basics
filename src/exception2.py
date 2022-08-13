#Linked List Program to Add and Delete Node Form Head, Tail, in Between Nodes.
class Node:
    """ Node Class having the data and pointer to the next Node"""
    def __init__(self,value):
        self.value=value
        self.nextnode=None

class LinkedList(object):
    """ Linked List Class to point the value and the next nond"""
    def __init__(self):
        self.head=None

    #Adding Node to the head of linked List
    def head_node(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            return
        crnt_node=node
        crnt_node.nextnode=self.head
        self.head=crnt_node

    # Adding New Node in between Node After the Previous Node
    def in_bw_node(self,prev_data,value):
        if prev_data is None:
            print('Can not add nodes in between of empty LinkedList')
            return
        n=self.head
        while n is not None:
            if n.value==prev_data:
                break
            n=n.nextnode
        new_node=Node(value)
        new_node.nextnode=n.nextnode
        n.nextnode=new_node

    # Adding New Node in between Node before the Previous Node
    def insert_before_node(self,prev_data,value):
        if prev_data is None:
            print('Can not add nodes in between of empty LinkedList')
            return
        p=self.head
        new_node=Node(value)
        while p is not None:
            if p.nextnode.value==prev_data:
                break
            p=p.nextnode
        new_node.nextnode=p.nextnode
        p.nextnode=new_node

    # Adding New Node in the last and last node is pointting to None
    def tail_node(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            return
        crnt_node=self.head
        while True:
            if crnt_node.nextnode is None:
                crnt_node.nextnode=node
                break
            crnt_node=crnt_node.nextnode

    # Deleting head node(1'st Node ) of the Linked List
    def del_head_node(self):
        if self.head is None:
            print('Can not delete Nodes from Empty Linked List')
            return
        crnt_node=self.head
        while self.head is not None:
            self.head=crnt_node.nextnode
            break
        crnt_node.nextnode=self.head.nextnode

    # Deleting the last Node of the linked List
    def del_tail_node(self):
        if self.head is None:
            print('Can not delete Nodes from Empty Linked List')
            return
        crnt_node=self.head
        while True:
            if crnt_node.nextnode.nextnode is None:
                crnt_node.nextnode=None
                break
            crnt_node=crnt_node.nextnode

    # Deleting the Node after given Node
    def del_in_bw_node(self,value):
        del_node=Node(value)
        if self.head is None:
            print('Can not delete Nodes from Empty Linked List')
            return
        crnt_node=self.head
        while  True:
            if crnt_node.value==del_node.value:
                break
            prev=crnt_node
            crnt_node=prev.nextnode
        prev.nextnode=crnt_node.nextnode
    # Pointing last Node to First Node
    def last_node_to_first_node(self):
        if self.head is None:
            print('Can not delete Nodes from Empty Linked List')
            return
        crnt_node=self.head
        while True:
            if  crnt_node.nextnode is None:
                print('head')
                last_node=self.head
                break
            crnt_node=crnt_node.nextnode
        crnt_node.nextnode=last_node

    # Method to print the Data
    def print_list(self):
        crnt_node=self.head
        while True:
            print(crnt_node.value,end='')
            if crnt_node.nextnode is self.head:
                break
            crnt_node = crnt_node.nextnode
            print('->', end='')


llist=LinkedList()
# llist.print_list()
llist.head_node(1)
llist.tail_node(2)
llist.tail_node(5)
llist.tail_node(10)
llist.last_node_to_first_node()
llist.print_list()