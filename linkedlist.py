#!/usr/bin/python3
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head, self.tail = head,head
        if head:
            self.length = 1
    
    def append(self, node):
        if not self.head:
            self.head = node
        self.tail.next = node
        self.tail = node
        self.length += 1
    
    def remove(self, val):
        current = self.head
        previous = None
        while current:
            if current.val == val:
                if not previous:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.length -= 1
                return val
            previous = current
            current = current.next
        return -1

    def print_list(self):
        current = self.head
        print("The current length of the list is {}".format(self.length))
        print("The val of the head is {} , and the tail is {}".format(self.head.val , self.tail.val))
        while current:
            print(current.val)
            current = current.next



def main():
    n1 = Node()
    ll = LinkedList(n1)
    n2 = Node(3)
    ll.append(n2)
    ll.print_list()
    ll.remove(0)
    ll.print_list()
    n3 = Node(4)
    n4 = Node(4)
    n5 = Node('a')
    ll.append(n3)
    ll.append(n4)
    ll.append(n5)
    ll.print_list()
    ll.remove('a')
    ll.print_list()
    val = 5
    if ll.remove(val) < 0:
        print("{} doesn't exist in the ll".format(val))
    ll.print_list()


    



if __name__ == '__main__':
    main()