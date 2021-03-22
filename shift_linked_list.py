# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    # Write your code here.
    temp = head
    n = 0
    while temp != None:
        n += 1
        temp = temp.next
    move = k % n
    if move == 0:
        return head
    to_move = n - move
    c = 0
    temp = head
    while c < to_move - 1:
        temp = temp.next
        c += 1
    next = temp.next
    temp.next = None
    temp2 = next
    while temp2.next != None:
        temp2 = temp2.next
    temp2.next = head
    return next


def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array


head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(5)
result = shiftLinkedList(head, 2)
array = linkedListToArray(result)

expected = [4, 5, 0, 1, 2, 3]
