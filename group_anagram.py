#!/usr/bin/env python3
from linkedlist import LinkedList, Node

def main():
    head = Node(1)
    ll = LinkedList(head)
    ll.append(Node('b'))
    ll.print_list()




if __name__ == '__main__':
    main()