"""
Sample implementation of singly linked list
"""


class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverseLinkedList(head):

    curr = head
    prev = None
    next = None

    while curr:
        next = curr.nextnode
        curr.nextnode = prev
        prev = curr
        curr = next

    return prev


"""
Function to reverese every n node in a linked list
"""
def reversethreenodes(head, n):

    print(head.value)
    current = head
    previous = None
    next = None

    count = 1
    while current:
        print("count = %d " % count)
        if count == n:
            reversethreenodes(next, n)
            count = 1
        else:
            next = current.nextnode
            current.nextnode = previous
            previous = current
            current = next
            count += 1
    return previous

def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    # d = Node(4)
    # e = Node(5)
    # f = Node(6)
    # g = Node(7)


    # Connect nodes
    a.nextnode = b
    b.nextnode = c
    # c.nextnode = d
    # d.nextnode = e
    # e.nextnode = f
    # f.nextnode = g

    # rev = reverseLinkedList(a)
    rev = reversethreenodes(a, 3)
    while rev:
        print(rev.value)
        rev = rev.nextnode


if __name__ == '__main__':
    main()
