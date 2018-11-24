"""
Sample implementation of singly linked list
"""


class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, elem):
        tmpnode = Node(elem)
        tmpnode.nextnode = self.head
        self.head = tmpnode

    def append(self, elem):
        if self.head is None:
            self.insert(elem)
        else:
            tmpnode = self.head
            while tmpnode.nextnode is not None:
                tmpnode = tmpnode.nextnode

            newnode = Node(elem)
            tmpnode.nextnode = newnode

    def reverseList(self):
        current = self.head
        next = None
        prev = None

        while current is not None:
            next = current.nextnode
            current.nextnode = prev
            prev = current
            current = next

        return prev

    def reverseEveryKnode(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        while(current is not None and count < k):
            next = current.nextnode
            current.nextnode = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.nextnode = self.reverseEveryKnode(next, k)

        return prev

    def printlist(self):
        if self.head is None:
            print("empty list")

        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp = tmp.nextnode

    def __len__(self):
        length = 0
        tmp = self.head
        while tmp:
            length += 1
            tmp = tmp.nextnode
        return length


def main():
    slinklist = LinkedList()

    # slinklist.insert(1)
    # slinklist.insert(2)
    # slinklist.insert(3)

    slinklist.insert(1)
    slinklist.insert(2)
    slinklist.insert(3)
    slinklist.insert(4)
    slinklist.insert(5)
    slinklist.insert(6)

    print("\n---- List is -----\n")
    slinklist.printlist()

    print("\n---- Now List is -----\n")
    slinklist.printlist()

    # print("\n---- reverseList is -----\n")
    # slinklist.head = slinklist.reverseEveryKnode(slinklist.head, 3)
    # slinklist.printlist()


    # print("\n---- reverseList is -----\n")
    # rev = slinklist.reverseList()
    # while rev:
    #     print(rev.value)
    #     rev = rev.nextnode


if __name__ == '__main__':
    main()
