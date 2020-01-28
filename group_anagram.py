#!/usr/bin/env python3
from linkedlist import LinkedList, Node
import time
import string
import random
# O(n^2)
def is_anagram_by_comparison(s1 , s2):
    # check if len match. for each char in s1, check if matching in s2.
    if len(s1) != len(s2):
        return False
    
    if len(s2) == 0:
        return True

    # turn s2 into ll for easy removal
    it = iter(s2)
    ll = LinkedList(Node(next(it)))
    for c in it:
        ll.append(Node(c))
    
    # for each char in string1, remove from string2 if exist
    for c in s1:
        if ll.remove(c) < 0:
            return False
    
    return True

# O(n^4), horrible!
def get_groups_of_anagrams_using_comparison(li):
    start = time.time()
    # turn list to ll for easy removal
    it = iter(li)
    ll = LinkedList(Node(next(it)))
    for st in it:
        ll.append(Node(st))
    li = []
    while ll.length:
        inner_li = []
        current = ll.head
        st = current.val
        while current:
            st2 = current.val
            current = current.next
            if is_anagram_by_comparison(st,st2):
                inner_li.append(st2)
                ll.remove(st2)
        li.append(inner_li)
    end = time.time()
    print("This function finished in {} seconds ".format(end-start))
    return li

#O(n*clog(c))
def get_groups_of_anagrams_using_sort_and_map(li):
    start = time.time()
    hm = {}
    for i in li:
        sorted_key = ''.join(sorted(i))
        if sorted_key not in hm:
            hm[sorted_key] = []
        hm[sorted_key].append(i)
    end = time.time()
    print("This function finished in {} seconds ".format(end-start))
    return list(hm.values())

    
def generate_inputs_of_same_length(length , num_of_inputs):
    letters = string.ascii_lowercase
    li = []
    for _ in range(num_of_inputs):
        s = ""
        for _ in range(length):
            s += random.choice(letters)
        li.append(s)
    return li
 
            



def main():
    li = generate_inputs_of_same_length(4 ,1000)
    print("The list is {} and contains {} words".format(li,len(li)))
    # print(get_groups_of_anagrams_using_comparison(li))
    print(get_groups_of_anagrams_using_sort_and_map(li))


if __name__ == '__main__':
    main()