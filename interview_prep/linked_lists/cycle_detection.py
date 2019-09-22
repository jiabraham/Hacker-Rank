"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    
    if head == None:
        return False
    repeat = {}
    cur = head
    while cur:
        if cur.data in repeat:
            return True
        else:
            repeat[cur.data] = 1
        cur = cur.next
    
    return False
